#!/usr/bin/env python3
#
# MEASURE THE BIAS & RESPONSIVENESS OF REDISTRICTING PLAN, USING JOHN NAGLE'S METHOD
#
# For example:
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

    # Save the input file names
    plan.vpi_csv = os.path.basename(vpi_csv)
    plan.parms_txt = os.path.basename(parms_txt)

    # Read the input files, and add the data to the Plan object
    plan.vpi_by_district, plan.two_party_by_district = read_vpi(vpi_csv)
    parms = read_parms(parms_txt, FIELD_SPECS)
    for i in parms:
        setattr(plan, i, parms[i])

    # Auto-construct output file names from the input files
    # Grab an input file name to pattern the output file names
    file_pattern = os.path.basename(vpi_csv)
    parts = [x.strip() for x in file_pattern.split('-')]
    xx = parts[0]
    plan_name = parts[1]
    election = parts[2]
    d = '-'

    # Add a '2' to the new extended points.csv file
    points_csv = xx + d + plan_name + d + election + d + 'points2.csv'
    analysis_csv = xx + d + plan_name + d + election + d + 'analysis.csv'

    # # Save the analysis output file name
    # plan.analysis_csv = os.path.basename(analysis_csv)

    points_csv = os.path.abspath(points_csv)
    analysis_csv = os.path.abspath(analysis_csv)

    # Evaluate the plan & echo the human-friendly analytics report
    evaluate_plan(plan)

    if verbose:
        # Echo a user-friendly version of the analysis to STDOUT
        print_analysis(plan)

    # Write the output files into the same directory as the input files
    write_points_csv(plan, points_csv)
    # TODO - Uncomment next
    # write_analysis_txt(plan, analysis_csv)

# READ THE TWO INPUT FILES


def read_vpi(vpi_csv):
    """
    The VPI file might have a second column of two-party vote totals for analyzing
    turnout bias.
    """
    # HACK - Reading these separately is a bit of a hack. If we need to do something
    #   with the two-party vote total, I should combine values into tuples by district.
    vpi_by_district = []
    two_party_by_district = []
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

                if 'TWO-PARTY' in row:
                    two_party_by_district.append(row['TWO-PARTY'])
    except Exception as e:
        print("Exception reading VPI-by-CD.csv")
        sys.exit(e)

    return vpi_by_district, two_party_by_district


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
        print("Vf, D-Sf, R-Sf, B_GSf, D-Sf-Pfptp, D-Sf-Uprob, D-Sf-Ufptp", file=handle)

        for i in range(0, plan.n_sv_pts):
            vf_d, s_d = plan.d_sv_pts[i]
            _, s_r = plan.r_sv_pts[i]
            _, b_gs = plan.b_gs_pts[i]
            # Additional points
            _, s_d_pf = plan.d_sv_pf_pts[i]
            _, s_d_up = plan.d_sv_up_pts[i]
            _, s_d_uf = plan.d_sv_uf_pts[i]

            # Convert #'s of seats to seat shares
            sf_d = s_d / plan.districts
            sf_r = s_r / plan.districts
            b_gsf = b_gs / plan.districts
            # Additional points
            sf_d_pf = s_d_pf / plan.districts
            sf_d_uf = s_d_uf / plan.districts
            sf_d_up = s_d_up / plan.districts

            print("{0:.6f},".format(vf_d),
                  "{0:.6f},".format(sf_d),
                  "{0:.6f},".format(sf_r),
                  "{0:+.6f},".format(b_gsf),
                  # Additional points
                  "{0:.6f},".format(sf_d_pf),
                  "{0:.6f}".format(sf_d_up),
                  "{0:.6f},".format(sf_d_uf),
                  file=handle
                  )


def write_analysis_txt(plan, analytics_csv):
    with open(analytics_csv, 'w') as handle:
        print("{0}-{1}, {2}, Definition".format(plan.state,
                                                plan.name, plan.election_model), file=handle)
        print("state<V>, {0:.6f}, Statewide fractional D vote".format(
            plan.statewide_vote_share), file=handle)
        print(
            "t-bias, {0:.6f}, state<V> minus average district D vote".format(
                round(plan.turnout_bias, 6) + 0), file=handle)
        print("S-fptp, {0:.0f}, Seats from first past the post".format(
            plan.actual_D_seats), file=handle)
        print("S<V>est, {0:.6f}, Seats at state<V>".format(
            plan.predicted_D_seats), file=handle)
        print("S50est, {0:.6f}, Seats at V=0.5".format(
            plan.predicted_D_seats_at_half_vote_share), file=handle)
        print("BS<V>, {0:.6}, % Geometric Seat Bias at statewide<V>".format(
            plan.b_gs_pct * 100), file=handle)
        print(
            "BS50, {0:.6f}, % Simple Bias at V=0.5".format(plan.seats_bias_pct * 100), file=handle)
        print("BV<V>, {0:.6f}, % Vote Bias at statewide<V>".format(
            plan.b_gv * 100), file=handle)
        print("BV50, {0:.6f}, % Vote Bias at V=0.5".format(
            plan.votes_bias * 100), file=handle)
        print("R<V>, {0:.6f}, Responsiveness as a slope in S(V) at statewide<V>".format(
            plan.responsiveness), file=handle)
        print("R50, {0:.6f}, Responsiveness as a slope in S(V) at V=0.5".format(
            plan.r_at_half_vote_share), file=handle)
        print("RD<V>, {0:.6f}, Number of responsive districts at statewide <V>".format(
            plan.responsive_districts), file=handle)
        print("RD50, {0:.6f}, Number of responsive districts at V=0.5".format(
            plan.number_rd_at_half_share), file=handle)
        print("EG<V>fpp, {0:.6f}, Efficiency Gap at state<V> using first past post S".format(
            plan.eg * 100), file=handle)
        print("EG<V>S(V), {0:.6f}, Efficiency Gap at state<V> using estimated S(V)".format(
            plan.eg_predicted_at_V * 100), file=handle)


# END


# Execute the script
main()
