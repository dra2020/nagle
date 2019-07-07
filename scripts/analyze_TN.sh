#!/bin/bash
#
# ANALYZE A BATCH OF PLANS
#
# For example: 
#
# analyze_TN.sh

START=$(date +"%T")

echo
echo "Started analyzing plans @ $START ..."
echo

echo "... TN-2012-2004P ..."
cd TN-2012-2004P
analyze_plan.py TN-2012-2004P-VPI-by-CD.csv TN-2012-2004P-parms.txt
cd ..

echo "... TN-2012-2006G ..."
cd TN-2012-2006G
analyze_plan.py TN-2012-2006G-VPI-by-CD.csv TN-2012-2006G-parms.txt
cd ..

echo "... TN-2012-2006S ..."
cd TN-2012-2006S
analyze_plan.py TN-2012-2006S-VPI-by-CD.csv TN-2012-2006S-parms.txt
cd ..

echo "... TN-2012-2008P ..."
cd TN-2012-2008P
analyze_plan.py TN-2012-2008P-VPI-by-CD.csv TN-2012-2008P-parms.txt
cd ..

echo "... TN-2012-2008S ..."
cd TN-2012-2008S
analyze_plan.py TN-2012-2008S-VPI-by-CD.csv TN-2012-2008S-parms.txt
cd ..

echo "... TN-2012-2010-12D ..."
cd TN-2012-2010-12D
analyze_plan.py TN-2012-2010-12D-VPI-by-CD.csv TN-2012-2010-12D-parms.txt
cd ..

echo "... TN-2012-2010G ..."
cd TN-2012-2010G
analyze_plan.py TN-2012-2010G-VPI-by-CD.csv TN-2012-2010G-parms.txt
cd ..

echo "... TN-2012-2012P ..."
cd TN-2012-2012P
analyze_plan.py TN-2012-2012P-VPI-by-CD.csv TN-2012-2012P-parms.txt
cd ..

echo "... TN-2012-2012S ..."
cd TN-2012-2012S
analyze_plan.py TN-2012-2012S-VPI-by-CD.csv TN-2012-2012S-parms.txt
cd ..

END=$(date +"%T")
echo
echo "... finished @ $END."
echo
