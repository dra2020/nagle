#!/usr/bin/env python3
#
# DATA FOR WARRINGTON'S HYPOTHETICAL ELECTIONS


import numpy as np

statewide_vote_share = 0.633217
vpi_by_district = [
    0.384407, 0.643145, 0.620664, 0.789455,
    0.671242, 0.562937, 0.773399, 0.632344
]
shifted_vote_share = 0.25

shifted_vpis = shift_districts_uniformly(statewide_vote_share,
                                         vpi_by_district, shifted_vote_share)
shift_districts(statewide_vote_share,
                vpi_by_district, shifted_vote_share)
shift_districts(statewide_vote_share,
                vpi_by_district, shifted_vote_share,
                proportional=False)

est_statewide_seats_fptp(vpi_by_district)

#

# From Warrington:

# 3
# data for hypothetical elections

# looks like a classic gerrymander
# - SG will think it's dandy (it's not)
hypo_NC = [0.35, 0.37, 0.39, 0.41, 0.43, 0.45, 0.47, 0.71, 0.71, 0.71]

# classic gerrymander by a minority party
# - LG will think it's dandy (it's not)
hypo_wd = [x - .20 for x in hypo_NC]

# sweep
# - looks kind of like Massachusetts
# - Dec is undefined
hypo_MA = [0.55, 0.57, 0.59, 0.61, 0.63, 0.65, 0.67, 0.69, 0.71, 0.73]

# uncompetitive
# - bipartisan gerrymander - 4 + 6 seats
# - MM will hate it
hypo_un = [0.25, 0.28, 0.31, 0.34, 0.60, 0.63, 0.66, 0.69, 0.72, 0.75]

hypo_wide = [0.1, 0.13, 0.16, 0.19, 0.70, 0.73, 0.76, 0.79, 0.82, 0.85]

# uncompetitive but shifted closer to Republicans (so Dem gerrymander)
hypo_sh = [x - 0.08 for x in hypo_un]

# very competitive in some races
# - Bias, EG will hate this one
# - similar to 1994 WA 11
hypo_co = [0.43, 0.45, 0.47, 0.51, 0.51, 0.51, 0.51, 0.57, 0.61, 0.63]

new_co = [0.49, 0.495, 0.505, 0.505, 0.505, 0.505,
          0.51, 0.545, 0.545, 0.545, 0.545, 0.545]

# At 50% already, so bias won't shift at all and will indicate the other way
hypo_ev = [0.41, 0.43, 0.45, 0.515, 0.515, 0.515, 0.515, 0.56, 0.59, 0.60]

# Miscalibrated
hypo_mi = [x-0.03 for x in [0.35, 0.4, 0.45,
                            0.58, 0.60, 0.62, 0.64, 0.77, 0.82, 0.87]]

hypo_tri = [x+0.06 for x in [0.24, 0.27, 0.475,
                             0.485, 0.495, 0.505, 0.515, 0.525, 0.73, 0.76]]

cubic = [x+0.07 for x in [0.10, 0.30, 0.44,
                          0.48, 0.495, 0.505, 0.52, 0.56, 0.70, 0.9]]

# evenly matched a-proportional distributions
prop1 = [0.2 for i in range(
    5)] + list(np.linspace(0.24, 0.76, 13)) + [0.8 for i in range(5)]
prop2 = np.linspace(0.25, 0.75, 25)
prop3 = np.linspace(0.34, 0.66, 25)

# proportionality
hypo_1 = [x + 0.1 for x in prop1]
hypo_2 = [x + 0.1 for x in prop2]
hypo_3 = [x + 0.1 for x in prop3]

hypo_elecs = {'Classic': hypo_NC, 'Inverted': hypo_wd, 'Sweep': hypo_MA, 'Uncompetitive': hypo_un,
              'Anti-majoritarian': hypo_sh, '1-proportionality': hypo_1, '2-proportionality': hypo_2,
              '3-proportionality': hypo_3, 'Competitive': new_co,
              'Competitive even': hypo_ev, 'Very uncompetitive': hypo_wide, 'Cubic': cubic}

# in a particular order
# hypo_elec_list = ['one_prop','two_prop','three_prop','comp','sweep','uncomp','shifted','classic','inverted']
hypo_elec_list = ['1-proportionality', '2-proportionality', '3-proportionality', 'Sweep',
                  'Competitive', 'Competitive even', 'Uncompetitive', 'Very uncompetitive',
                  'Cubic', 'Anti-majoritarian', 'Classic', 'Inverted']

sens_list = ['2-proportionality', 'Competitive', 'Uncompetitive', 'Classic']
sens_list2 = ['1-proportionality',
              '3-proportionality', 'Sweep', 'Competitive even']
sens_list3 = ['Very uncompetitive', 'Cubic', 'Anti-majoritarian', 'Inverted']

# 3
