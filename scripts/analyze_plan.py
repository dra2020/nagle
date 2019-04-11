#!/usr/bin/env python3
#
# MEASURE THE BIAS & RESPONSIVENESS OF REDISTRICTING PLAN, USING JOHN NAGLE'S METHOD
#
# For example, from the root data directory:
#
# analyze_plan.py examples/MD-2018-2012P-VPI-by-CD.csv examples/MD-2018-2012P-parms.txt
# analyze_plan.py examples/PA-SCOPA-7S-VPI-by-CD.csv examples/PA-SCOPA-7S-parms.txt
# analyze_plan.py examples/MA-2012-2010A-VPI-by-CD.csv examples/MA-2012-2010A-parms.txt
#
# For documentation, type:
#
# analyze_plan.py -h

from nagle import *

import sys
import os
import argparse
import csv
from collections import defaultdict


# Parse the command line arguments


def main():
    parser = argparse.ArgumentParser(description='Analyze a plan')
    parser.add_argument('vpi_csv', help='VPI by CD .csv')
    parser.add_argument('parms_txt', help='Parameters')
    parser.add_argument('-v', '--verbose', dest='verbose',
                        action='store_true', help='verbose mode')

    args = parser.parse_args()

    vpi_csv = os.path.abspath(args.vpi_csv)
    parms_txt = os.path.abspath(args.parms_txt)

    verbose = args.verbose

    plan = Plan()

    # Read the input files, and add the data to the Plan object
    plan.vpi_by_district = read_vpi(vpi_csv)
    parms = read_parms(parms_txt, FIELD_SPECS)
    for i in parms:
        setattr(plan, i, parms[i])

    # Evaluate the plan & echo the human-friendly analytics report
    evaluate_plan(plan)
    print_analytics(plan)

    # Auto-construct file names from the input files
    # Grab an input file name to pattern the output file names
    file_pattern = os.path.basename(vpi_csv)
    parts = [x.strip() for x in file_pattern.split('-')]
    xx = parts[0]
    plan_name = parts[1]
    election = parts[2]
    d = '-'

    points_csv = xx + d + plan_name + d + election + d + 'points.csv'
    analytics_txt = xx + d + plan_name + d + election + d + 'analytics.txt'

    points_csv = os.path.abspath(points_csv)
    analytics_txt = os.path.abspath(analytics_txt)

    # Write the output files into the same directory as the input files
    write_points_csv(plan, points_csv)
    write_analytics_txt(plan, analytics_txt)


# READ THE TWO INPUT FILES


def read_vpi(vpi_csv):
    vpi_by_district = []
    try:
        # Get the full path to the .csv
        vpi_csv = os.path.expanduser(vpi_csv)

        with open(vpi_csv, mode="r", encoding="utf-8-sig") as f_input:
            csv_file = csv.DictReader(f_input)

            # Process each row in the .csv file
            for row in csv_file:
                # Subset the row to the desired columns
                district_id = row['DISTRICT']
                vpi_fraction = float(row['VPI'])

                # and write it out into a dictionary
                vpi_by_district.append(vpi_fraction)
    except Exception as e:
        print("Exception reading VPI-by-CD.csv")
        sys.exit(e)

    return vpi_by_district


# Fields in parms.text file
FIELD_SPECS = [
    ('state', str),
    ('districts', int),
    ('name', str),
    ('election_model', str),
    ('statewide_vote_share', float)
]


def read_parms(parms_txt, field_specs):
    parms_txt = os.path.expanduser(parms_txt)
    parms = defaultdict(dict)

    try:
        i = 0
        with open(parms_txt, mode="r", encoding="utf-8-sig") as f_input:
            for line in f_input:
                line = line.strip('\n')
                fields = line.split(':')
                # Use the field_spec name vs. the name in the file
                field_name = field_specs[i][0]
                # field_name = fields[0].strip(" \"")
                field_value = fields[1].strip(" \"")

                field_type = field_specs[i][1]
                field_value = field_type(field_value)

                parms[field_name] = field_value

                i += 1
    except Exception as e:
        print("Exception reading parms.txt")
        sys.exit(e)

    return parms

# WRITE THE TWO OUTPUT FILES


def write_points_csv(plan, points_csv):
    # A clone of print_all_points()
    with open(points_csv, 'w') as handle:
        print("Vf, D-Sf, R-Sf, B_GSf", file=handle)

        for i in range(0, plan.n_sv_pts):
            vf_d, s_d = plan.d_sv_pts[i]
            _, s_r = plan.r_sv_pts[i]
            _, b_gs = plan.b_gs_pts[i]

            # Convert #'s of seats to seat shares
            sf_d = s_d / plan.districts
            sf_r = s_r / plan.districts
            b_gsf = b_gs / plan.districts

            print("{0:.6f},".format(vf_d),
                  "{0:.6f},".format(sf_d),
                  "{0:.6f},".format(sf_r),
                  "{0:+.6f}".format(b_gsf),
                  file=handle
                  )


def write_analytics_txt(plan, analytics_txt):
    with open(analytics_txt, 'w') as handle:
        print("SeatsBiasSimple:          ",
              "{0:+0.2f}".format(plan.seats_bias), file=handle)
        print("SeatsBiasSimplePercent:   ",
              "{0:+.2%}".format(plan.seats_bias_pct), file=handle)
        print("SeatsBiasGeometric:       ",
              "{0:+0.2f}".format(plan.b_gs), file=handle)
        print("SeatsBiasGeometricPercent:",
              "{0:+.2%}".format(plan.b_gs_pct), file=handle)
        print("VotesBiasSimple:          ",
              "{0:+.2%}".format(plan.votes_bias), file=handle)
        print("VotesBiasSimpleGeometric: ",
              "{0:+.2%}".format(plan.b_gv), file=handle)
        print("Responsiveness:           ",
              " {0:0.2f}".format(plan.responsiveness), file=handle)
        print("ResponsiveDistricts:      ",
              " {0:0.2f}".format(plan.responsive_districts), file=handle)
        print("AverageVPI:               ",
              " {0:0.6f}".format(plan.average_VPI), file=handle)

# END


# Execute the script
main()
