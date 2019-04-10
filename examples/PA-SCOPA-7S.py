#!/usr/bin/env python3
#
# The SCOPA plan using 7S election data. Can be evaluated by hand.

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

evaluate_plan(plan)
print_all_points(plan)
print_analytics(plan)

# plot_partial_sv_curve(plan, "SCOPA S-V Curve")

#
