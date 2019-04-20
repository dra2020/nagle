#!/usr/bin/env python3
#
# THE PA SCOPA PLAN USING 7S ELECTION DATA.
#
# Use this to validate the D S(V) curve.

from nagle import *


plan = Plan()

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

plan.vpi_csv = "PA-SCOPA-7S.py"
plan.parms_txt = "PA-SCOPA-7S.py"
plan.analysis_txt = "STDOUT"

#

print_plan(plan)

evaluate_plan(plan)

print_points(plan, plan.d_sv_pts)

print_analysis(plan)
# TODO - DELETE: print_analytics(plan)

plot_partial_sv_curve(plan, "SCOPA S-V Curve")

#
