#!/usr/bin/env python3

import sys
import time

import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np


# A simple container to hold input & output data


class Plan:
    def __init__(plan):
        pass


# Print the plan details


def print_plan(plan):
    print("DISTRICT,", "VPI")

    i = 0
    for vpi in plan.vpi_by_district:
        i += 1
        print("{0:2},".format(i), "{0:.6f}".format(vpi))
    print()

# Print the estimated points for an S(V) or B_GS curve


def print_points(plan, points, sign=False):
    print("Vf", "Sf")

    for vote_share, seats in points:
        seat_share = seats / plan.districts
        if sign:
            print("{0:.6f},".format(vote_share), "{0:+.6f}".format(
                seat_share))
        else:
            print("{0:.6f},".format(vote_share), "{0:.6f}".format(
                seat_share))

# Print the estimated points for the D S(V), R S(V), and B_GS curves


def print_all_points(plan):
    print("Vf, D-Sf, R-Sf, B_GSf")

    for i in range(0, plan.n_sv_pts):
        vf_d, s_d = plan.d_sv_pts[i]
        _, s_r = plan.r_sv_pts[i]
        _, b_gs = plan.b_gs_pts[i]

        # Convert #'s of seats to seat shares
        sf_d = s_d / plan.districts
        sf_r = s_r / plan.districts
        b_gsf = b_gs / plan.districts

        print("{0:.6f},".format(vf_d),
              "{0:.6f},".format(sf_d),
              "{0:.6f},".format(sf_r),
              "{0:+.6f}".format(b_gsf)
              )


def print_analysis(plan, handle=None):
    if (handle is None):
        handle = sys.stdout

    print(file=handle)
    print("ANALYSIS - Captured in", plan.analysis_txt,
          "@", time.strftime('%l:%M%p %Z on %b %d, %Y'), file=handle)
    print("===============================================================================", file=handle)
    print(file=handle)
    print("For VPI by CD in {0}".format(plan.vpi_csv),
          "and these parameters in {0}:".format(plan.parms_txt), file=handle)
    print(file=handle)

    print("* Number of districts:         ",
          "{0:.0f}".format(plan.districts), file=handle)

    print("* Actual seats:                 D =", "{0:02.2f}".format(
        plan.actual_D_seats), ", R =", "{0:02.2f}".format(plan.actual_R_seats), file=handle)
    print("* Predicted seats:              D =", "{0:02.2f}".format(
        plan.predicted_D_seats), ", R =", "{0:02.2f}".format(plan.predicted_R_seats), file=handle)

    print("* Statewide D vote share (V):  ",
          "{0:.6f}".format(plan.statewide_vote_share), file=handle)
    print("* Average VPI:                 ",
          "{0:0.6f}".format(plan.average_VPI), file=handle)
    print("* Difference (turnout bias):  ",
          "{0:+0.6f}".format(plan.turnout_bias), file=handle)
    print(file=handle)

    print("Results @ V =                  ", "{0:.6f}".format(
        plan.statewide_vote_share), "|   0.50", file=handle)
    print("-------------------------------------------------------------------------------", file=handle)

    print("* Seats Bias (#):             ",
          "{0:+01.2f}".format(plan.b_gs), "    | ", "{0:+01.2f}".format(plan.seats_bias), file=handle)
    print("             (%):             ", "{0:+#02.2%}".format(
        plan.b_gs_pct), "   | ", "{0:+#02.2%}".format(plan.seats_bias_pct), file=handle)

    print("* Votes Bias (%):             ",
          "{0:+#02.2%}".format(plan.b_gv), "   | ", "{0:+#02.2%}".format(plan.votes_bias), file=handle)

    print("* Responsiveness:              ",
          "{0:02.2f}".format(plan.responsiveness), "    |  ", "{0:02.2f}".format(plan.r_at_half_vote_share), file=handle)
    print("* Responsive Districts (#):    ",
          "{0:02.2f}".format(plan.responsive_districts), "    |  ", "{0:02.2f}".format(plan.number_rd_at_half_share), file=handle)
    rd_pct = plan.responsiveness / plan.districts
    rd_pct_at_half = plan.number_rd_at_half_share / plan.districts
    print("                       (%):    ",
          "{0:#02.2%}".format(rd_pct), "   | ", "{0:#02.2%}".format(rd_pct_at_half), file=handle)
    print("* Efficiency Gap (%):        ",
          "{0:+#02.2%}".format(plan.eg), "   | ", "{0:+#02.2%}".format(plan.eg_at_half_share), file=handle)
    print(file=handle)


# Plot an S/V Curve


def plot_partial_sv_curve(plan, title):
    sv_pts = plan.d_sv_pts
    name = plan.name
    total_seats = plan.districts
    half_seats = float(total_seats / 2)
    half_votes = 0.5

    # Unzip the S/V curve points into separate lists
    x = [x for x, y in sv_pts]
    y = [y for x, y in sv_pts]

    # Convert #'s of seats to fractions of total seats [0–1],
    # so that the responsiveness slope is correct visually.
    y_pct = [float(s / total_seats) for s in y]

    # Make horizontal and verticle rules
    ry = [(half_seats / total_seats) for x, y in sv_pts]
    rx = [half_votes for x, y in sv_pts]

    # Make a vertical rule at the statewide vote share
    rx2 = [plan.statewide_vote_share for x, y in sv_pts]

    sv_curve = go.Scatter(
        x=x,
        y=y_pct,
        mode='markers+lines',
        name='S/V Curve',
        marker=dict(
            size=5
        )
    )

    h_rule = go.Scatter(
        x=x,
        y=ry,
        name='Half the seats',
        mode='lines',
        line=dict(
            width=1,
            dash='dash'
        )
    )

    v_rule = go.Scatter(
        x=rx,
        y=y,
        name='Half the votes',
        mode='lines',
        line=dict(
            width=1,
            dash='dot'
        )
    )

    v_rule2 = go.Scatter(
        x=rx2,
        y=y,
        name='Statewide vote share',
        mode='lines',
        line=dict(
            width=1,
            dash='dashdot'
        )
    )

    layout = go.Layout(
        title='S/V Curve for ' + name + ' Plan',
        xaxis=dict(
            title="D Vote Share",
            range=[0.36, 0.58],
            tickmode='linear',
            ticks='outside',
            tick0=0.36,
            dtick=0.02
        ),
        yaxis=dict(
            title="D Seat Share",
            range=[0.36, 0.58],
            tickmode='linear',
            ticks='outside',
            tick0=0.36,
            dtick=0.02
        )
    )

    data = [sv_curve, h_rule, v_rule, v_rule2]
    fig = go.Figure(data=data, layout=layout)

    py.plot(fig, filename=title)

# Plot both S/V Curves


def plot_full_sv_curves(plan, title):
    d_sv_pts = plan.d_sv_pts
    r_sv_pts = plan.r_sv_pts
    name = plan.name
    total_seats = plan.districts

    # Unzip the D S/V curve points into separate lists
    v_d = [x for x, y in d_sv_pts]
    s_d = [y for x, y in d_sv_pts]

    # Convert #'s of seats to fractions of total seats [0–1].
    s_d = [float(s / total_seats) for s in s_d]

    # Unzip the R S/V curve points into separate lists
    v_r = [x for x, y in r_sv_pts]
    s_r = [y for x, y in r_sv_pts]

    # Convert #'s of seats to fractions of total seats [0–1].
    s_r = [float(s / total_seats) for s in s_r]

    # Make horizontal and vertical rules @ 50%
    r_x = [0.0, 0.5, 1.0]
    r_y = [0.0, 0.5, 1.0]
    r_s = [0.5, 0.5, 0.5]
    r_v = [0.5, 0.5, 0.5]

    d_sv_curve = go.Scatter(
        x=v_d,
        y=s_d,
        mode='lines',
        name='Democrats',
        marker=dict(
            size=5
        )
    )

    r_sv_curve = go.Scatter(
        x=v_r,
        y=s_r,
        mode='lines',
        name='Republicans',
        marker=dict(
            size=5
        )
    )

    h_rule = go.Scatter(
        x=r_x,
        y=r_s,
        name='Half the seats',
        mode='lines',
        line=dict(
            width=1,
            dash='dash'
        )
    )

    v_rule = go.Scatter(
        x=r_v,
        y=r_y,
        name='Half the votes',
        mode='lines',
        line=dict(
            width=1,
            dash='dot'
        )
    )

    layout = go.Layout(
        title='S/V Curves for ' + name + ' Plan',
        xaxis=dict(
            title="V (fraction)",
            range=[0.0, 1.0],
            tickmode='linear',
            ticks='outside',
            tick0=0.0,
            dtick=0.1
        ),
        yaxis=dict(
            title="S (fraction)",
            range=[0.0, 1.0],
            tickmode='linear',
            ticks='outside',
            tick0=0.0,
            dtick=0.1
        )
    )

    data = [d_sv_curve, r_sv_curve, h_rule, v_rule]
    fig = go.Figure(data=data, layout=layout)

    py.plot(fig, filename=title)

# Plot Figure 1 from Nagle's paper
# NOTE - Evaluate est_seat_probability() and est_district_responsiveness()
#   first manually, then evaluate this function definition and execute it.


def plot_figure_1():
    B = np.linspace(0.35, 0.65, 100)

    A = [(1 - est_seat_probability(i)) for i in B]
    r = [est_district_responsiveness(i) for i in B]

    trace1 = go.Scatter(
        x=B,
        y=A,
        mode='lines',
        name='Probability of party A seat',
        marker=dict(
            size=3
        )
    )

    trace2 = go.Scatter(
        x=B,
        y=r,
        mode='lines',
        name='Responsiveness fraction',
        marker=dict(
            size=3
        )
    )

    layout = go.Layout(
        title='Seat Probability & Responsiveness',
        xaxis=dict(
            title="Fraction that voted for party B",
            range=[0.35, 0.65],
            tickmode='linear',
            ticks='outside',
            tick0=0.35,
            dtick=0.05
        ),
        yaxis=dict(
            range=[0.0, 1.0],
            tickmode='linear',
            ticks='outside',
            tick0=0,
            dtick=0.25
        )
    )

    data = [trace1, trace2]
    fig = go.Figure(data=data, layout=layout)

    py.plot(fig, filename="Figure-1")


# Define vote shifts over the middle of the S/V curve, including V = 50%


def shift_range(statewide_vote_share):
    shift_lower = 25 / 100
    shift_upper = 75 / 100
    shift_step = (1/100) / 2    # In 1/2% increments
    epsilon = 1.0e-12

    return np.arange(shift_lower, shift_upper + epsilon, shift_step)

# Find the point that brackets a value on the lower end


def lower_bracket(sv_curve_pts, value, v_or_s):
    LAST = -1

    smaller_pts = []
    for pt in sv_curve_pts:
        if pt[v_or_s] <= value:
            smaller_pts.append(pt)
    lower_pt = smaller_pts[LAST]

    return lower_pt

# Find the point that brackets a value on the upper end


def upper_bracket(sv_curve_pts, value, v_or_s):
    upper_pt = None
    for pt in sv_curve_pts:
        if pt[v_or_s] >= value:
            upper_pt = pt
            break
    return upper_pt

#
