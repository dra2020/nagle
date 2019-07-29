#!/bin/bash
#
# ANALYZE A BATCH OF PLANS
#
# For example: 
#
# analyze_PA.sh

START=$(date +"%T")

echo
echo "Started analyzing plans @ $START ..."
echo

echo "... PA-2012-2004P ..."
cd PA-2012-2004P
analyze_plan.py PA-2012-2004P-VPI-by-CD.csv PA-2012-2004P-parms.txt
cd ..

echo "... PA-2012-2006G ..."
cd PA-2012-2006G
analyze_plan.py PA-2012-2006G-VPI-by-CD.csv PA-2012-2006G-parms.txt
cd ..

echo "... PA-2012-2006S ..."
cd PA-2012-2006S
analyze_plan.py PA-2012-2006S-VPI-by-CD.csv PA-2012-2006S-parms.txt
cd ..

echo "... PA-2012-2008AG ..."
cd PA-2012-2008AG
analyze_plan.py PA-2012-2008AG-VPI-by-CD.csv PA-2012-2008AG-parms.txt
cd ..

echo "... PA-2012-2008P ..."
cd PA-2012-2008P
analyze_plan.py PA-2012-2008P-VPI-by-CD.csv PA-2012-2008P-parms.txt
cd ..

echo "... PA-2012-2010-12D ..."
cd PA-2012-2010-12D
analyze_plan.py PA-2012-2010-12D-VPI-by-CD.csv PA-2012-2010-12D-parms.txt
cd ..

echo "... PA-2012-2010G ..."
cd PA-2012-2010G
analyze_plan.py PA-2012-2010G-VPI-by-CD.csv PA-2012-2010G-parms.txt
cd ..

echo "... PA-2012-2010S ..."
cd PA-2012-2010S
analyze_plan.py PA-2012-2010S-VPI-by-CD.csv PA-2012-2010S-parms.txt
cd ..

echo "... PA-2012-2012AG ..."
cd PA-2012-2012AG
analyze_plan.py PA-2012-2012AG-VPI-by-CD.csv PA-2012-2012AG-parms.txt
cd ..

echo "... PA-2012-2012P ..."
cd PA-2012-2012P
analyze_plan.py PA-2012-2012P-VPI-by-CD.csv PA-2012-2012P-parms.txt
cd ..

echo "... PA-2012-2012S ..."
cd PA-2012-2012S
analyze_plan.py PA-2012-2012S-VPI-by-CD.csv PA-2012-2012S-parms.txt
cd ..

END=$(date +"%T")
echo
echo "... finished @ $END."
echo
