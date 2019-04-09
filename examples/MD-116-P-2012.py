#!/usr/bin/env python3
#
# The MD 116th CD's, using 2012 Presidential election results. Can be evaluated by hand.

from nagle import *

plan = Plan()

plan.state = "MD"
plan.districts = 8
plan.name = "2018 Districts"
plan.election_model = "2012 President"
plan.statewide_vote_share = 0.633217
plan.vpi_by_district = [
    0.384407, 0.643145, 0.620664, 0.789455,
    0.671242, 0.562937, 0.773399, 0.632344
]

#

evaluate_plan(plan)
print_analytics(plan)
print_all_points(plan)

# plot_partial_sv_curve(plan, "MD-116-P2012")

#
