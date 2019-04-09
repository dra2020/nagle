#!/usr/bin/env python3
#
# MEASURE THE BIAS & RESPONSIVENESS OF REDISTRICTING PLAN, USING JOHN NAGLE'S METHOD
#
# For example, from the root data directory:
#
# analyze_plan.py MD-116-P-2012-VPI-by-CD.csv MD-116-P-2012-parms.txt
#
# For documentation, type:
#
# analyze_plan.py -h

#
# TODO - Kenshi: I can't get *any* of these imports (and others) to work!
#   I just want to use the nagle stuff in these scripts ...
#

# from context import nagle

# from nagle import *
# from nagle import *

# from method import *
# from helpers import *
# from utils import *
# from settings import *

import sys
import os
import argparse
import csv

# print("sys.path =>", sys.path)


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

    print("TODO - Read input files")

    hardcode_plan(plan)

    print("TODO - Evaluate the plan")
    evaluate_plan(plan)

    print("TODO - Write the output files")
    print("TODO - Combine points")
    print_analytics(plan)


# Simulate a script, until I get imports to work
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
