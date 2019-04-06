#!/usr/bin/env python3
#
# TEMPORARY SCAFFOLDING, UNTIL I GET IMPORTS WORKING RIGHT

# TODO - I CAN'T GET THESE IMPORTS TO WORK HERE EITHER

from .method import *
from .helpers import *


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


plan = Plan()

print("TODO - Read input files")

hardcode_plan(plan)

print("TODO - Evaluate the plan")
evaluate_plan(plan)

print("TODO - Write the output files")
print("TODO - Combine points")
print_analytics(plan)

#


# The SCOPA plan using Nagle's 7s election model
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

#

evaluate_plan(plan)

print_points(plan, plan.d_sv_pts)
print_points(plan, plan.r_sv_pts)
print_points(plan, plan.b_gs_pts, sign=True)

print_analytics(plan)

plot_partial_sv_curve(plan, "SCOPA S-V Curve")

#
