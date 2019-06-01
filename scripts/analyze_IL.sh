#!/bin/bash
#
# ANALYZE A BATCH OF PLANS
#
# For example: 
#
# analyze_IL.sh

START=$(date +"%T")

echo
echo "Started analyzing plans @ $START ..."
echo

echo "... IL-2012-2004P ..."
cd IL-2012-2004P
analyze_plan.py IL-2012-2004P-VPI-by-CD.csv IL-2012-2004P-parms.txt
cd ..

echo "... IL-2012-2006AG ..."
cd IL-2012-2006AG
analyze_plan.py IL-2012-2006AG-VPI-by-CD.csv IL-2012-2006AG-parms.txt
cd ..

echo "... IL-2012-2006C ..."
cd IL-2012-2006C
analyze_plan.py IL-2012-2006C-VPI-by-CD.csv IL-2012-2006C-parms.txt
cd ..

echo "... IL-2012-2006G ..."
cd IL-2012-2006G
analyze_plan.py IL-2012-2006G-VPI-by-CD.csv IL-2012-2006G-parms.txt
cd ..

echo "... IL-2012-2006SoS ..."
cd IL-2012-2006SoS
analyze_plan.py IL-2012-2006SoS-VPI-by-CD.csv IL-2012-2006SoS-parms.txt
cd ..

echo "... IL-2012-2006T ..."
cd IL-2012-2006T
analyze_plan.py IL-2012-2006T-VPI-by-CD.csv IL-2012-2006T-parms.txt
cd ..

echo "... IL-2012-2008-10D ..."
cd IL-2012-2008-10D
analyze_plan.py IL-2012-2008-10D-VPI-by-CD.csv IL-2012-2008-10D-parms.txt
cd ..

echo "... IL-2012-2008P ..."
cd IL-2012-2008P
analyze_plan.py IL-2012-2008P-VPI-by-CD.csv IL-2012-2008P-parms.txt
cd ..

echo "... IL-2012-2008S ..."
cd IL-2012-2008S
analyze_plan.py IL-2012-2008S-VPI-by-CD.csv IL-2012-2008S-parms.txt
cd ..

echo "... IL-2012-2010AG ..."
cd IL-2012-2010AG
analyze_plan.py IL-2012-2010AG-VPI-by-CD.csv IL-2012-2010AG-parms.txt
cd ..

echo "... IL-2012-2010C ..."
cd IL-2012-2010C
analyze_plan.py IL-2012-2010C-VPI-by-CD.csv IL-2012-2010C-parms.txt
cd ..

echo "... IL-2012-2010G ..."
cd IL-2012-2010G
analyze_plan.py IL-2012-2010G-VPI-by-CD.csv IL-2012-2010G-parms.txt
cd ..

echo "... IL-2012-2010S ..."
cd IL-2012-2010S
analyze_plan.py IL-2012-2010S-VPI-by-CD.csv IL-2012-2010S-parms.txt
cd ..

echo "... IL-2012-2010SoS ..."
cd IL-2012-2010SoS
analyze_plan.py IL-2012-2010SoS-VPI-by-CD.csv IL-2012-2010SoS-parms.txt
cd ..

echo "... IL-2012-2010T ..."
cd IL-2012-2010T
analyze_plan.py IL-2012-2010T-VPI-by-CD.csv IL-2012-2010T-parms.txt
cd ..

echo "... IL-2012-2012P ..."
cd IL-2012-2012P
analyze_plan.py IL-2012-2012P-VPI-by-CD.csv IL-2012-2012P-parms.txt
cd ..

END=$(date +"%T")
echo
echo "... finished @ $END."
echo
