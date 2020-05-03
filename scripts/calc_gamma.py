#!/usr/bin/env python3
#
# A QUICK & DIRTY SCRIPT TO CALCULATE THE NEW GAMMA MEASURE
#
# For documentation, type:
#
# calc_gamma.py -h

from nagle import *

import sys
import os
import argparse
import csv
from collections import defaultdict


# Parse the command line arguments


def main():
    parser = argparse.ArgumentParser(description='Calculate gamma for a plan')
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

    # Evaluate the plan & echo the human-friendly analytics report
    evaluate_plan(plan)
    # Echo the new gamma measure
    print_gamma(plan)

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


# END


# Execute the script
main()
