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

cd CA
calc_gamma.py CA-2012-VPI-by-CD.csv CA-2012-parms.txt

cd ..

cd CO
calc_gamma.py CO-2012-VPI-by-CD.csv CO-2012-parms.txt

cd ..

cd IL
calc_gamma.py IL-2012-VPI-by-CD.csv IL-2012-parms.txt

cd ..

cd MA
calc_gamma.py MA-2012-VPI-by-CD.csv MA-2012-parms.txt

cd ..

cd MD
calc_gamma.py MD-2012-VPI-by-CD.csv MD-2012-parms.txt

cd ..

cd NC
calc_gamma.py NC-2012-VPI-by-CD.csv NC-2012-parms.txt

cd ..

cd OH
calc_gamma.py OH-2012-VPI-by-CD.csv OH-2012-parms.txt

cd ..

cd PA
calc_gamma.py PA-2012-VPI-by-CD.csv PA-2012-parms.txt

cd ..

cd SC
calc_gamma.py SC-2012-VPI-by-CD.csv SC-2012-parms.txt

cd ..

cd TN
calc_gamma.py TN-2012-VPI-by-CD.csv TN-2012-parms.txt

cd ..

cd TX
calc_gamma.py TX-2012-VPI-by-CD.csv TX-2012-parms.txt

cd ..

END=$(date +"%T")
echo
echo "... finished @ $END."
echo
