#!/usr/bin/env python3
#
# MEASURE THE BIAS & RESPONSIVENESS OF REDISTRICTING PLAN, USING JOHN NAGLE'S METHOD
#
# For example, from the root data directory:
#
# analyze_plan.py examples/MD-2018-2012P-VPI-by-CD.csv examples/MD-2018-2012P-parms.txt
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

    # VERIFY SYSTEM PATHS
    # print("sys.path =>", sys.path)

    # VERIFY THE TWO INPUT FILES
    # print("VPI-by-CD:", vpi_csv)
    # print("Parms:", parms_txt)
    # vpi_csv = '/Users/alecramsay/src/nagle/examples/MD-2018-2012P-VPI-by-CD.csv'
    # parms_txt = '/Users/alecramsay/src/nagle/examples/MD-2018-2012P-parms.txt'

    # Create a plan object
    plan = Plan()
    # Read the VPI by district input & add it to the Plan object
    plan.vpi_by_district = read_vpi(vpi_csv)
    # Read the parameters input & add it to the Plan object
    parms = read_parms(parms_txt, FIELD_SPECS)
    for i in parms:
        print("Parm =", i, "value =", parms[i])
        setattr(plan, i, parms[i])

    # hardcode_plan(plan)  # REMOVE

    evaluate_plan(plan)

    # TODO - Create file names
    points_csv = 'MD-2018-2012P-points.csv'
    analytics_txt = 'MD-2018-2012P-analytics.txt'
    points_csv = os.path.abspath(points_csv)
    analytics_txt = os.path.abspath(analytics_txt)

    # TODO - Redirect this output to files or write proper files
    print_all_points(plan)
    print_analytics(plan)


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

# TODO - WRITE THE TWO OUTPUT FILES


def write_points_csv(plan, points_csv):
    points_csv = os.path.expanduser(points_csv)

    with open(points_csv, 'w') as handle:
        fieldnames = ['Vf', 'D-Sf', 'R-Sf', 'B_GSf']
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()

        for row in plan_csv_dict:
            writer.writerow(row)


def write_analytics_txt(plan_csv_dict, map_csv):
    map_csv = os.path.expanduser(map_csv)

    with open(map_csv, 'w') as handle:
        fieldnames = ['GEOID', 'DISTRICT']
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in plan_csv_dict:
            writer.writerow(row)


# DELETE
# def write_map_csv(plan_csv_dict, map_csv):
#     map_csv = os.path.expanduser(map_csv)

#     with open(map_csv, 'w') as handle:
#         fieldnames = ['GEOID', 'DISTRICT']
#         writer = csv.DictWriter(handle, fieldnames=fieldnames)
#         writer.writeheader()
#         for row in plan_csv_dict:
#             writer.writerow(row)

# SIMULATE READING THE INPUT FILES


def hardcode_plan(plan):
    # The SCOPA plan using Nagle's 7s election model
    plan.state = "PA"
    plan.districts = 18
    plan.name = "SCOPA"
    plan.election_model = "7s"
    plan.statewide_vote_share = 0.5487
    plan.vpi_by_district = [
        0.922, 0.793, 0.684, 0.621, 0.6, 0.566,
        0.552, 0.526, 0.513, 0.511, 0.495, 0.495,
        0.476, 0.454, 0.423, 0.393, 0.39, 0.371
    ]

# END


# Execute the script
main()
