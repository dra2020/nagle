#!/usr/bin/env python3
#
# MD 2018 CD'S, USING 2012 PRESIDENTIAL ELECTION RESULTS.

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

plan.vpi_csv = "MD-2018-2012P.py"
plan.parms_txt = "MD-2018-2012P.py"
plan.analysis_txt = "STDOUT"

#

print_plan(plan)

evaluate_plan(plan)

print_points(plan, plan.d_sv_pts)

print_analysis(plan)
# TODO - DELETE: print_analytics(plan)

plot_partial_sv_curve(plan, "MD-2018-2012P")

#
