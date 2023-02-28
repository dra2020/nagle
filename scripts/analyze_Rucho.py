#!/usr/bin/env python3
#
# MEASURE THE BIAS & RESPONSIVENESS OF REDISTRICTING PLAN, USING JOHN NAGLE'S METHOD
#
# For example:
#
# analyze_Rucho.py -d NC-Rucho-actuals-VPI-by-CD.csv -p NC-Rucho-actuals-parms.txt
# analyze_Rucho.py -d NC-Rucho-composite-VPI-by-CD.csv -p NC-Rucho-composite-parms.txt
#
# For documentation, type:
#
# analyze_Rucho.py -h

from nagle import *

import sys
import os
import argparse
from argparse import ArgumentParser, Namespace
import csv
from csv import DictReader
from collections import defaultdict
from typing import Any


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Analyze the Rucho plan responsiveness"
    )
    parser.add_argument(
        "-d",
        "--districts",
        default="NC-Rucho-composite-VPI-by-CD.csv",
        help="VPI-by-CD.csv",
        type=str,
    )
    parser.add_argument(
        "-p",
        "--parms",
        default="NC-Rucho-composite-parms.txt",
        help="parms.txt",
        type=str,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    args: Namespace = parse_args()

    root_dir: str = "examples/"

    vpi_csv: str = os.path.abspath(root_dir + args.districts)
    parms_txt: str = os.path.abspath(root_dir + args.parms)

    verbose: bool = args.verbose

    plan: Plan = Plan()
    plan.vpi_csv = os.path.basename(vpi_csv)
    plan.parms_txt = os.path.basename(parms_txt)

    plan.vpi_by_district = read_vpi(vpi_csv)
    parms: defaultdict[str, Any] = read_parms(parms_txt, FIELD_SPECS)

    for i in parms:
        setattr(plan, i, parms[i])

    # TODO - HERE
    evaluate_Rucho(plan)

    pass


# READ THE TWO INPUT FILES


def read_vpi(vpi_csv) -> list:
    vpi_by_district = []
    try:
        vpi_csv: str = os.path.expanduser(vpi_csv)

        with open(vpi_csv, mode="r", encoding="utf-8-sig") as f_input:
            csv_file: DictReader[str] = csv.DictReader(f_input)

            for row in csv_file:
                district_id: str = row["DISTRICT"]
                vpi_fraction: float = float(row["VPI"])

                vpi_by_district.append(vpi_fraction)

    except Exception as e:
        print("Exception reading VPI-by-CD.csv")
        sys.exit(e)

    return vpi_by_district


# Fields in parms.text file
FIELD_SPECS = [
    ("state", str),
    ("districts", int),
    ("name", str),
    ("election_model", str),
    ("statewide_vote_share", float),
]


def read_parms(parms_txt, field_specs) -> defaultdict[str, Any]:
    parms_txt: str = os.path.expanduser(parms_txt)
    parms: defaultdict[str, Any] = defaultdict(str)

    try:
        i: int = 0
        with open(parms_txt, mode="r", encoding="utf-8-sig") as f_input:
            for line in f_input:
                line: str = line.strip("\n")
                fields: list[str] = line.split(":")
                # Use the field_spec name vs. the name in the file
                field_name: str = field_specs[i][0]
                # field_name = fields[0].strip(" \"")
                field_value: str = fields[1].strip(' "')

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
