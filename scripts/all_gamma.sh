#!/bin/bash
#
# ANALYZE A BATCH OF PLANS
#
# For example: 
#
# all_gamma.sh

START=$(date +"%T")

echo
echo "Started analyzing plans @ $START ..."
echo

# Start at ~/nagle
cd research/elections
echo State, Plan, Election, r, g

#CA

cd CA
calc_gamma.py CA-2012-VPI-by-CD.csv CA-2012-parms.txt

cd ..

# CO

cd CO
calc_gamma.py CO-2012-VPI-by-CD.csv CO-2012-parms.txt
cd CO-2012-2004P
calc_gamma.py CO-2012-2004P-VPI-by-CD.csv CO-2012-2004P-parms.txt
cd ..

cd CO-2012-2006AG
calc_gamma.py CO-2012-2006AG-VPI-by-CD.csv CO-2012-2006AG-parms.txt
cd ..

cd CO-2012-2006G
calc_gamma.py CO-2012-2006G-VPI-by-CD.csv CO-2012-2006G-parms.txt
cd ..

cd CO-2012-2006SoS
calc_gamma.py CO-2012-2006SoS-VPI-by-CD.csv CO-2012-2006SoS-parms.txt
cd ..

cd CO-2012-2008P
calc_gamma.py CO-2012-2008P-VPI-by-CD.csv CO-2012-2008P-parms.txt
cd ..

cd CO-2012-2008S
calc_gamma.py CO-2012-2008S-VPI-by-CD.csv CO-2012-2008S-parms.txt
cd ..

cd CO-2012-2010-12D
calc_gamma.py CO-2012-2010-12D-VPI-by-CD.csv CO-2012-2010-12D-parms.txt
cd ..

cd CO-2012-2010AG
calc_gamma.py CO-2012-2010AG-VPI-by-CD.csv CO-2012-2010AG-parms.txt
cd ..

cd CO-2012-2010G
calc_gamma.py CO-2012-2010G-VPI-by-CD.csv CO-2012-2010G-parms.txt
cd ..

cd CO-2012-2010S
calc_gamma.py CO-2012-2010S-VPI-by-CD.csv CO-2012-2010S-parms.txt
cd ..

cd CO-2012-2010SoS
calc_gamma.py CO-2012-2010SoS-VPI-by-CD.csv CO-2012-2010SoS-parms.txt
cd ..

cd CO-2012-2012P
calc_gamma.py CO-2012-2012P-VPI-by-CD.csv CO-2012-2012P-parms.txt
cd ..
cd ..

# IL

cd IL
calc_gamma.py IL-2012-VPI-by-CD.csv IL-2012-parms.txt

cd ..

# MA

cd MA
calc_gamma.py MA-2012-VPI-by-CD.csv MA-2012-parms.txt

cd ..

# MD
cd MD
calc_gamma.py MD-2012-VPI-by-CD.csv MD-2012-parms.txt

cd ..

# NC
cd NC
calc_gamma.py NC-2012-VPI-by-CD.csv NC-2012-parms.txt

cd ..

#OH
cd OH
calc_gamma.py OH-2012-VPI-by-CD.csv OH-2012-parms.txt

cd ..

# PA
cd PA
calc_gamma.py PA-2012-VPI-by-CD.csv PA-2012-parms.txt

cd ..

#SC
cd SC
calc_gamma.py SC-2012-VPI-by-CD.csv SC-2012-parms.txt

cd ..

# TN

cd TN
calc_gamma.py TN-2012-VPI-by-CD.csv TN-2012-parms.txt

cd ..

# TX
cd TX
calc_gamma.py TX-2012-VPI-by-CD.csv TX-2012-parms.txt

cd ..

END=$(date +"%T")
echo
echo "... finished @ $END."
echo
