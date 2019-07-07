#!/bin/bash
#
# ANALYZE A BATCH OF PLANS
#
# For example: 
#
# analyze_MD.sh

START=$(date +"%T")

echo
echo "Started analyzing plans @ $START ..."
echo

echo "... MD-2010-2004P ..."
cd MD-2010-2004P
analyze_plan.py MD-2010-2004P-VPI-by-CD.csv MD-2010-2004P-parms.txt
cd ..

echo "... MD-2010-2006AG ..."
cd MD-2010-2006AG
analyze_plan.py MD-2010-2006AG-VPI-by-CD.csv MD-2010-2006AG-parms.txt
cd ..

echo "... MD-2010-2006C ..."
cd MD-2010-2006C
analyze_plan.py MD-2010-2006C-VPI-by-CD.csv MD-2010-2006C-parms.txt
cd ..

echo "... MD-2010-2006G ..."
cd MD-2010-2006G
analyze_plan.py MD-2010-2006G-VPI-by-CD.csv MD-2010-2006G-parms.txt
cd ..

echo "... MD-2010-2006S ..."
cd MD-2010-2006S
analyze_plan.py MD-2010-2006S-VPI-by-CD.csv MD-2010-2006S-parms.txt
cd ..

echo "... MD-2010-2008P ..."
cd MD-2010-2008P
analyze_plan.py MD-2010-2008P-VPI-by-CD.csv MD-2010-2008P-parms.txt
cd ..

echo "... MD-2010-2010C ..."
cd MD-2010-2010C
analyze_plan.py MD-2010-2010C-VPI-by-CD.csv MD-2010-2010C-parms.txt
cd ..

echo "... MD-2010-2010AG ..."
cd MD-2010-2010AG
analyze_plan.py MD-2010-2010AG-VPI-by-CD.csv MD-2010-2010AG-parms.txt
cd ..

echo "... MD-2010-2010D ..."
cd MD-2010-2010D
analyze_plan.py MD-2010-2010D-VPI-by-CD.csv MD-2010-2010D-parms.txt
cd ..

echo "... MD-2010-2010G ..."
cd MD-2010-2010G
analyze_plan.py MD-2010-2010G-VPI-by-CD.csv MD-2010-2010G-parms.txt
cd ..

echo "... MD-2010-2012P ..."
cd MD-2010-2012P
analyze_plan.py MD-2010-2012P-VPI-by-CD.csv MD-2010-2012P-parms.txt
cd ..

echo "... MD-2010-2012S ..."
cd MD-2010-2012S
analyze_plan.py MD-2010-2012S-VPI-by-CD.csv MD-2010-2012S-parms.txt
cd ..

END=$(date +"%T")
echo
echo "... finished @ $END."
echo
