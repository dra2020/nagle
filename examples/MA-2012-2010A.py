#!/usr/bin/env python3
#
# A MA REDISTRICTING PLAN, USING NAGLE'S EXTENDED METHOD
#
# Use this to validate B_GS.

from nagle import *


plan = Plan()

plan.state = "MA"
plan.districts = 9
plan.name = "Massachusetts"
plan.election_model = "State Auditor"
plan.statewide_vote_share = 0.521777
plan.vpi_by_district = [
    0.455, 0.464, 0.475, 0.478, 0.491, 0.494, 0.529, 0.555, 0.755
]

#

print_plan(plan)

evaluate_plan(plan)

print_points(plan, plan.d_sv_pts)
print_points(plan, plan.r_sv_pts)
print_points(plan, plan.b_gs_pts, sign=True)

print_analytics(plan)

plot_full_sv_curves(plan, "MA S-V Curves")

#
