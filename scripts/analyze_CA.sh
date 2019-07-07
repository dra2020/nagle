#!/bin/bash
#
# ANALYZE A BATCH OF PLANS
#
# For example: 
#
# analyze_CA.sh

START=$(date +"%T")

echo
echo "Started analyzing plans @ $START ..."
echo

echo "... CA-2012-2008P ..."
cd CA-2012-2008P
analyze_plan.py CA-2012-2008P-VPI-by-CD.csv CA-2012-2008P-parms.txt
cd ..

echo "... CA-2012-2010-12D ..."
cd CA-2012-2010-12D
analyze_plan.py CA-2012-2010-12D-VPI-by-CD.csv CA-2012-2010-12D-parms.txt
cd ..

echo "... CA-2012-2010AG ..."
cd CA-2012-2010AG
analyze_plan.py CA-2012-2010AG-VPI-by-CD.csv CA-2012-2010AG-parms.txt
cd ..

echo "... CA-2012-2010C ..."
cd CA-2012-2010C
analyze_plan.py CA-2012-2010C-VPI-by-CD.csv CA-2012-2010C-parms.txt
cd ..

echo "... CA-2012-2010G ..."
cd CA-2012-2010G
analyze_plan.py CA-2012-2010G-VPI-by-CD.csv CA-2012-2010G-parms.txt
cd ..

echo "... CA-2012-2010SoS ..."
cd CA-2012-2010SoS
analyze_plan.py CA-2012-2010SoS-VPI-by-CD.csv CA-2012-2010SoS-parms.txt
cd ..

echo "... CA-2012-2010T ..."
cd CA-2012-2010T
analyze_plan.py CA-2012-2010T-VPI-by-CD.csv CA-2012-2010T-parms.txt
cd ..

echo "... CA-2012-2012P ..."
cd CA-2012-2012P
analyze_plan.py CA-2012-2012P-VPI-by-CD.csv CA-2012-2012P-parms.txt
cd ..

echo "... CA-2012-2012S ..."
cd CA-2012-2012S
analyze_plan.py CA-2012-2012S-VPI-by-CD.csv CA-2012-2012S-parms.txt
cd ..

END=$(date +"%T")
echo
echo "... finished @ $END."
echo
