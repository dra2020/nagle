#!/usr/bin/env python3

from math import erf, sqrt, isclose
from scipy.interpolate import interp1d
import numpy as np

from .helpers import *


# Infer an S/V curve, using a proportional shift


def infer_sv_points(statewide_vote_share, vpi_by_district):
    sv_curve_pts = []
    vpis_at_half_share = []

    for shifted_vote_share in shift_range(statewide_vote_share):
        shifted_vpis = shift_districts_proportionally(statewide_vote_share,
                                                      vpi_by_district,
                                                      shifted_vote_share)
        shifted_seats = est_statewide_seats(shifted_vpis)
        sv_curve_pts.append((shifted_vote_share, shifted_seats))

        # Squirrel away the inferred VPIs by district at V = 0.5
        if (isclose(shifted_vote_share, 0.5)):
            vpis_at_half_share = shifted_vpis

    return sv_curve_pts, vpis_at_half_share

# Shift district VPI's proportionally (vs. "uniform swing" assumption)


def shift_districts_proportionally(statewide_vote_share, vpi_by_district,
                                   shifted_vote_share):
    if shifted_vote_share < statewide_vote_share:
        # Shift down: D's to R's
        proportion = shifted_vote_share / statewide_vote_share
        shifted_vpis = [(v * proportion) for v in vpi_by_district]
    elif shifted_vote_share > statewide_vote_share:
        # Shift up: R's to D's
        proportion = (1 - shifted_vote_share) / (1 - statewide_vote_share)
        shifted_vpis = [(1 - (1 - v) * proportion) for v in vpi_by_district]
    else:
        # No shift: shift = actual
        shifted_vpis = vpi_by_district

    return shifted_vpis

# Estimate the statewide seats, given VPI's by district


def est_statewide_seats(vpi_by_district):
    return sum([est_seat_probability(vpi) for vpi in vpi_by_district])

# Estimate the probability of a seat win for district, given a VPI


def est_seat_probability(vpi):
    return 0.5 * (1 + erf((vpi - 0.50) / (0.02 * sqrt(8))))

# Estimate the S/V seats measure of bias (@ V = 50%)


def est_seats_bias(sv_curve_pts, total_seats):
    d_seats = d_seats_at_half_share(sv_curve_pts)
    r_seats = total_seats - d_seats

    return (r_seats - d_seats) / 2.0


def d_seats_at_half_share(sv_curve_pts):
    close_pts = [pt for pt in sv_curve_pts if isclose(pt[0], 0.5)]
    _, d_seats = next(iter(close_pts))

    return d_seats

# Instead expressed as a percentage of the # of districts


def est_seats_bias_pct(seats_bias, total_seats):
    return seats_bias / float(total_seats)

# Interpolate the S/V votes measure of bias (for half the seats)


def est_votes_bias(sv_curve_pts, total_seats):
    half_seats = float(total_seats) / 2.0

    x = [x for x, y in sv_curve_pts]
    y = [y for x, y in sv_curve_pts]
    fn = interp1d(y, x, kind='cubic')

    return fn(half_seats) - 0.50

# Estimate responsiveness (R) at the statewide vote share


def est_responsiveness(statewide_vote_share, sv_curve_pts, total_seats):
    VOTE_SHARE = 0

    V1, S1 = lower_bracket(sv_curve_pts, statewide_vote_share, VOTE_SHARE)
    V2, S2 = upper_bracket(sv_curve_pts, statewide_vote_share, VOTE_SHARE)

    # NOTE - To get a proper slope, normalize the seat delta into a fraction!
    R = ((S2 - S1) / total_seats) / (V2 - V1)

    return R

# Estimate the number of responsive districts [R(d)], given a set of VPI's


def est_responsive_districts(vpi_by_district):
    return sum([est_district_responsiveness(vpi) for vpi in vpi_by_district])

# Estimate the responsiveness of a district, given a VPI


def est_district_responsiveness(vpi):
    return 1 - 4 * (est_seat_probability(vpi) - 0.5)**2

# Infer inverse S/V curve


def infer_inverse_sv_points(ndistricts, statewide_vote_share, sv_pts):
    inverse_sv_curve_pts = []

    for v_d, s_d in sv_pts:
        v_r = 1 - v_d
        s_r = ndistricts - s_d  # # of seats, not seat share!
        inverse_sv_curve_pts.append((v_r, s_r))

    inverse_sv_curve_pts = sorted(inverse_sv_curve_pts, key=lambda pt: [pt[0]])

    return inverse_sv_curve_pts

# Infer a Bias of Geometric Seats (B_GS) curve


def infer_geometric_seats_bias_points(n_pts, d_sv_pts, r_sv_pts):
    b_gs_pts = []

    for i in range(0, n_pts):
        v_r, s_r = r_sv_pts[i]
        v_d, s_d = d_sv_pts[i]

        # NOTE - By convention: '+' = R bias; '-' = D bias
        b_gs = 0.5 * (s_r - s_d)

        b_gs_pts.append((v_d, b_gs))

    return b_gs_pts

# Estimate geometric seats bias (@ V = statewide vote share)


def est_geometric_seats_bias(statewide_vote_share, b_gs_pts):
    x = [x for x, y in b_gs_pts]
    y = [y for x, y in b_gs_pts]
    fn = interp1d(x, y, kind='cubic')

    return fn(statewide_vote_share)

# Instead expressed as a percentage of the # of districts


def est_geometric_seats_bias_pct(b_gs, total_seats):
    return b_gs / float(total_seats)

# Estimate geometric votes bias (for the statewide seat share)


def est_geometric_votes_bias(d_sv_pts, r_sv_pts, statewide_seats):
    x = [x for x, y in r_sv_pts]
    y = [y for x, y in r_sv_pts]
    fn = interp1d(y, x, kind='cubic')

    v_r = fn(statewide_seats)

    x = [x for x, y in d_sv_pts]
    y = [y for x, y in d_sv_pts]
    fn = interp1d(y, x, kind='cubic')

    v_d = fn(statewide_seats)

    # NOTE - By convention: '+' = R bias; '-' = D bias
    return 0.5 * (v_d - v_r)

# Calculate the efficiency gap


def efficiency_gap(vote_share, seat_share):
    return (seat_share - 0.5) - (2 * (vote_share - 0.5))

# Execute the method


def evaluate_plan(plan):
    plan.statewide_seats = est_statewide_seats(plan.vpi_by_district)
    plan.d_sv_pts, plan.vpis_at_half_share = infer_sv_points(plan.statewide_vote_share,
                                                             plan.vpi_by_district)
    plan.r_sv_pts = infer_inverse_sv_points(
        plan.districts, plan.statewide_vote_share, plan.d_sv_pts)
    plan.n_sv_pts = len(plan.d_sv_pts)
    plan.b_gs_pts = infer_geometric_seats_bias_points(plan.n_sv_pts,
                                                      plan.d_sv_pts,
                                                      plan.r_sv_pts)

    plan.seats_bias = est_seats_bias(plan.d_sv_pts, plan.districts)
    plan.seats_bias_pct = est_seats_bias_pct(plan.seats_bias, plan.districts)

    plan.votes_bias = est_votes_bias(plan.d_sv_pts, plan.districts)

    plan.responsiveness = est_responsiveness(plan.statewide_vote_share,
                                             plan.d_sv_pts, plan.districts)
    plan.responsive_districts = est_responsive_districts(plan.vpi_by_district)

    plan.b_gs = est_geometric_seats_bias(
        plan.statewide_vote_share, plan.b_gs_pts)
    plan.b_gs_pct = est_geometric_seats_bias_pct(plan.b_gs, plan.districts)

    plan.b_gv = est_geometric_votes_bias(
        plan.d_sv_pts, plan.r_sv_pts, plan.statewide_seats)

    # Added these for research into norms for responsiveness

    plan.predicted_D_seats = est_statewide_seats(plan.vpi_by_district)
    plan.predicted_R_seats = plan.districts - plan.predicted_D_seats

    plan.actual_D_seats = sum(1 for v in plan.vpi_by_district if (v > 0.5))
    plan.actual_R_seats = plan.districts - plan.actual_D_seats

    plan.average_VPI = np.mean(plan.vpi_by_district)
    plan.turnout_bias = plan.statewide_vote_share - plan.average_VPI

    plan.r_at_half_vote_share = est_responsiveness(
        0.5, plan.d_sv_pts, plan.districts)

    plan.number_rd_at_half_share = est_responsive_districts(
        plan.vpis_at_half_share)

    plan.eg = efficiency_gap(plan.statewide_vote_share,
                             plan.actual_D_seats / plan.districts)

    d_seats = round(d_seats_at_half_share(plan.d_sv_pts))
    plan.eg_at_half_share = efficiency_gap(0.5, d_seats / plan.districts)

#
