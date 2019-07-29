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

echo "... NC-2012-2008A ..."
cd NC-2012-2008A
analyze_plan.py NC-2012-2008A-VPI-by-CD.csv NC-2012-2008A-parms.txt
cd ..

echo "... NC-2012-2008AG ..."
cd NC-2012-2008AG
analyze_plan.py NC-2012-2008AG-VPI-by-CD.csv NC-2012-2008AG-parms.txt
cd ..

echo "... NC-2012-2008G ..."
cd NC-2012-2008G
analyze_plan.py NC-2012-2008G-VPI-by-CD.csv NC-2012-2008G-parms.txt
cd ..

echo "... NC-2012-2008P ..."
cd NC-2012-2008P
analyze_plan.py NC-2012-2008P-VPI-by-CD.csv NC-2012-2008P-parms.txt
cd ..

echo "... NC-2012-2008S ..."
cd NC-2012-2008S
analyze_plan.py NC-2012-2008S-VPI-by-CD.csv NC-2012-2008S-parms.txt
cd ..

echo "... NC-2012-2008SoS ..."
cd NC-2012-2008SoS
analyze_plan.py NC-2012-2008SoS-VPI-by-CD.csv NC-2012-2008SoS-parms.txt
cd ..

echo "... NC-2012-2008T ..."
cd NC-2012-2008T
analyze_plan.py NC-2012-2008T-VPI-by-CD.csv NC-2012-2008T-parms.txt
cd ..

echo "... NC-2012-2010S ..."
cd NC-2012-2010S
analyze_plan.py NC-2012-2010S-VPI-by-CD.csv NC-2012-2010S-parms.txt
cd ..

echo "... NC-2012-2012A ..."
cd NC-2012-2012A
analyze_plan.py NC-2012-2012A-VPI-by-CD.csv NC-2012-2012A-parms.txt
cd ..

echo "... NC-2012-2012G ..."
cd NC-2012-2012G
analyze_plan.py NC-2012-2012G-VPI-by-CD.csv NC-2012-2012G-parms.txt
cd ..

echo "... NC-2012-2012D ..."
cd NC-2012-2012D
analyze_plan.py NC-2012-2012D-VPI-by-CD.csv NC-2012-2012D-parms.txt
cd ..

echo "... NC-2012-2012SoS ..."
cd NC-2012-2012SoS
analyze_plan.py NC-2012-2012SoS-VPI-by-CD.csv NC-2012-2012SoS-parms.txt
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
