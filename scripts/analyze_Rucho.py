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

    # TODO - HERE

    for i in parms:
        setattr(plan, i, parms[i])

    # Auto-construct output file names from the input files
    # Grab an input file name to pattern the output file names
    file_pattern = os.path.basename(vpi_csv)
    parts = [x.strip() for x in file_pattern.split("-")]
    xx = parts[0]
    plan_name = parts[1]
    election = parts[2]
    d = "-"

    # Add a '2' to the new extended points.csv file
    points_csv = xx + d + plan_name + d + election + d + "points2.csv"
    analysis_csv = xx + d + plan_name + d + election + d + "analysis.csv"

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
    write_analysis_txt(plan, analysis_csv)


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


# WRITE THE TWO OUTPUT FILES


def write_points_csv(plan, points_csv):
    # A clone of print_all_points()
    with open(points_csv, "w") as handle:
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

            print(
                "{0:.6f},".format(vf_d),
                "{0:.6f},".format(sf_d),
                "{0:.6f},".format(sf_r),
                "{0:+.6f},".format(b_gsf),
                # Additional points
                "{0:.6f},".format(sf_d_pf),
                "{0:.6f},".format(sf_d_up),
                "{0:.6f}".format(sf_d_uf),
                file=handle,
            )


def write_analysis_txt(plan, analytics_csv):
    with open(analytics_csv, "w") as handle:
        print(
            "{0}-{1}, {2}, Definition".format(
                plan.state, plan.name, plan.election_model
            ),
            file=handle,
        )
        print(
            "state<V>, {0:.6f}, Statewide fractional D vote".format(
                plan.statewide_vote_share
            ),
            file=handle,
        )
        print(
            "t-bias, {0:.6f}, state<V> minus average district D vote".format(
                round(plan.turnout_bias, 6) + 0
            ),
            file=handle,
        )
        print(
            "S-fptp, {0:.0f}, Seats from first past the post".format(
                plan.actual_D_seats
            ),
            file=handle,
        )
        print(
            "S<V>est, {0:.6f}, Seats at state<V>".format(plan.predicted_D_seats),
            file=handle,
        )
        print(
            "S50est, {0:.6f}, Seats at V=0.5".format(
                plan.predicted_D_seats_at_half_vote_share
            ),
            file=handle,
        )
        print(
            "BS<V>, {0:.6}, % Geometric Seat Bias at statewide<V>".format(
                plan.b_gs_pct * 100
            ),
            file=handle,
        )
        print(
            "BS50, {0:.6f}, % Simple Bias at V=0.5".format(plan.seats_bias_pct * 100),
            file=handle,
        )
        print(
            "BV<V>, {0:.6f}, % Vote Bias at statewide<V>".format(plan.b_gv * 100),
            file=handle,
        )
        print(
            "BV50, {0:.6f}, % Vote Bias at V=0.5".format(plan.votes_bias * 100),
            file=handle,
        )
        print(
            "R<V>, {0:.6f}, Responsiveness as a slope in S(V) at statewide<V>".format(
                plan.responsiveness
            ),
            file=handle,
        )
        print(
            "R50, {0:.6f}, Responsiveness as a slope in S(V) at V=0.5".format(
                plan.r_at_half_vote_share
            ),
            file=handle,
        )
        print(
            "RD<V>, {0:.6f}, Number of responsive districts at statewide <V>".format(
                plan.responsive_districts
            ),
            file=handle,
        )
        print(
            "RD50, {0:.6f}, Number of responsive districts at V=0.5".format(
                plan.number_rd_at_half_share
            ),
            file=handle,
        )
        print(
            "EG<V>fpp, {0:.6f}, Efficiency Gap at state<V> using first past post S".format(
                plan.eg * 100
            ),
            file=handle,
        )
        print(
            "EG<V>S(V), {0:.6f}, Efficiency Gap at state<V> using estimated S(V)".format(
                plan.eg_predicted_at_V * 100
            ),
            file=handle,
        )


# END


# Execute the script
main()
