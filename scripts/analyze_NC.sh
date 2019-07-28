#!/bin/bash
#
# ANALYZE A BATCH OF PLANS
#
# For example: 
#
# analyze_NC.sh

# TODO

START=$(date +"%T")

echo
echo "Started analyzing plans @ $START ..."
echo

echo "... NC-2012-2004P ..."
cd NC-2012-2004P
analyze_plan.py NC-2012-2004P-VPI-by-CD.csv NC-2012-2004P-parms.txt
cd ..

echo "... NC-2012-2006AG ..."
cd NC-2012-2006AG
analyze_plan.py NC-2012-2006AG-VPI-by-CD.csv NC-2012-2006AG-parms.txt
cd ..

echo "... NC-2012-2006C ..."
cd NC-2012-2006C
analyze_plan.py NC-2012-2006C-VPI-by-CD.csv NC-2012-2006C-parms.txt
cd ..

echo "... NC-2012-2006G ..."
cd NC-2012-2006G
analyze_plan.py NC-2012-2006G-VPI-by-CD.csv NC-2012-2006G-parms.txt
cd ..

echo "... NC-2012-2006SoS ..."
cd NC-2012-2006SoS
analyze_plan.py NC-2012-2006SoS-VPI-by-CD.csv NC-2012-2006SoS-parms.txt
cd ..

echo "... NC-2012-2006T ..."
cd NC-2012-2006T
analyze_plan.py NC-2012-2006T-VPI-by-CD.csv NC-2012-2006T-parms.txt
cd ..

echo "... NC-2012-2008-10D ..."
cd NC-2012-2008-10D
analyze_plan.py NC-2012-2008-10D-VPI-by-CD.csv NC-2012-2008-10D-parms.txt
cd ..

echo "... NC-2012-2008P ..."
cd NC-2012-2008P
analyze_plan.py NC-2012-2008P-VPI-by-CD.csv NC-2012-2008P-parms.txt
cd ..

echo "... NC-2012-2008S ..."
cd NC-2012-2008S
analyze_plan.py NC-2012-2008S-VPI-by-CD.csv NC-2012-2008S-parms.txt
cd ..

echo "... NC-2012-2010AG ..."
cd NC-2012-2010AG
analyze_plan.py NC-2012-2010AG-VPI-by-CD.csv NC-2012-2010AG-parms.txt
cd ..

echo "... NC-2012-2010C ..."
cd NC-2012-2010C
analyze_plan.py NC-2012-2010C-VPI-by-CD.csv NC-2012-2010C-parms.txt
cd ..

echo "... NC-2012-2010G ..."
cd NC-2012-2010G
analyze_plan.py NC-2012-2010G-VPI-by-CD.csv NC-2012-2010G-parms.txt
cd ..

echo "... NC-2012-2010S ..."
cd NC-2012-2010S
analyze_plan.py NC-2012-2010S-VPI-by-CD.csv NC-2012-2010S-parms.txt
cd ..

echo "... NC-2012-2010SoS ..."
cd NC-2012-2010SoS
analyze_plan.py NC-2012-2010SoS-VPI-by-CD.csv NC-2012-2010SoS-parms.txt
cd ..

echo "... NC-2012-2010T ..."
cd NC-2012-2010T
analyze_plan.py NC-2012-2010T-VPI-by-CD.csv NC-2012-2010T-parms.txt
cd ..

echo "... NC-2012-2012P ..."
cd NC-2012-2012P
analyze_plan.py NC-2012-2012P-VPI-by-CD.csv NC-2012-2012P-parms.txt
cd ..

END=$(date +"%T")
echo
echo "... finished @ $END."
echo
