#!/usr/bin/env python3
#
# PREPROCESS THE CENSUS DATA (PRODUCE JUST WHAT'S NEEDED)
#
# For example, from the root data directory:
#
# preprocess_census.py wip/nc/nc2010-TABBLOCK.csv preprocessed/nc/NC-2010-BLOCK-census.pkl
# preprocess_census.py wip/nc/nc2010-BG.csv preprocessed/nc/NC-2010-BG-census.pkl
# preprocess_census.py wip/nc/nc2010-TRACT.csv preprocessed/nc/NC-2010-TRACT-census.pkl
# preprocess_census.py wip/nc/nc2010-COUNTY.csv preprocessed/nc/NC-2010-COUNTY-census.pkl
#
# For documentation, type:
#
# preprocess_census.py -h

import os
import sys
import csv
import argparse
from collections import defaultdict

from utils import *

# Parse the command line arguments
# Analyze counties for a state and pickle a parms file of key value
def main():
    parser = argparse.ArgumentParser(description='Proprocess Census data.')
    parser.add_argument('census_csv', help='Census .csv to preprocess.')
    parser.add_argument('pickle_file', help='Pickled Census extract.')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='verbose mode')

    args = parser.parse_args()

    c_csv = os.path.abspath(args.census_csv)
    p_file = os.path.abspath(args.pickle_file)

    verbose = args.verbose

    # Extract the necessary info from the Census data
    census = extract_census(c_csv, p_file)

    if verbose:
        print("Census:")
        print(census)


# HELPER TO ANALYZE COUNTIES FOR A STATE
# Used by the analyze_counties.py script.
@time_function
def extract_census(c_csv, p_file):
    try:
        # READ STANDARD CENSUS DATA FROM A .CSV FILE
        census = read_census_csv(c_csv)
    except Exception as e:
        sys.exit(e)

    # PICKLE THE EXTRACTED DATA FOR FUTURE USE
    try:
        pickle_native(census, p_file)
    except Exception:
        sys.exit("Error pickling Census data.")

    return census


# TODO - Modify this to accommodate new analytics
def read_census_csv(census_csv):
    # Get the full path to the .csv
    census_csv = os.path.expanduser(census_csv)

    # Initialize an index of Census data by geo
    census_by_geo = defaultdict(dict)

    with open(census_csv) as f_input:
        csv_file = csv.DictReader(f_input)

        # Process each row in the .csv file
        for row in csv_file:
            # Subset the row to the desired columns
            geo_id = row['GEOID']
            county = row['COUNTY']
            total = int(row['TOTAL'])

            # Add a pre-computed 'MINORITY' column: non-white hispanics
            white = int(row['WHITE'])
            hispanic = int(row['HISPANIC'])
            minority = total - (white - hispanic)

            # and write it out into a dictionary entry as a tuple
            census_by_geo[geo_id] = (total, minority, county)

    return census_by_geo

# END


# Execute the script
main()
