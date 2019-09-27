#!/bin/bash
#
# ANALYZE A BATCH OF PLANS
#
# For example: 
#
# analyze_CO.sh

START=$(date +"%T")

echo
echo "Started analyzing plans @ $START ..."
echo

echo "... CO-2012-2004P ..."
cd CO-2012-2004P
analyze_plan.py CO-2012-2004P-VPI-by-CD.csv CO-2012-2004P-parms.txt
cd ..

echo "... CO-2012-2006AG ..."
cd CO-2012-2006AG
analyze_plan.py CO-2012-2006AG-VPI-by-CD.csv CO-2012-2006AG-parms.txt
cd ..

echo "... CO-2012-2006G ..."
cd CO-2012-2006G
analyze_plan.py CO-2012-2006G-VPI-by-CD.csv CO-2012-2006G-parms.txt
cd ..

echo "... CO-2012-2006SoS ..."
cd CO-2012-2006SoS
analyze_plan.py CO-2012-2006SoS-VPI-by-CD.csv CO-2012-2006SoS-parms.txt
cd ..

echo "... CO-2012-2008P ..."
cd CO-2012-2008P
analyze_plan.py CO-2012-2008P-VPI-by-CD.csv CO-2012-2008P-parms.txt
cd ..

echo "... CO-2012-2008S ..."
cd CO-2012-2008S
analyze_plan.py CO-2012-2008S-VPI-by-CD.csv CO-2012-2008S-parms.txt
cd ..

echo "... CO-2012-2010-12D ..."
cd CO-2012-2010-12D
analyze_plan.py CO-2012-2010-12D-VPI-by-CD.csv CO-2012-2010-12D-parms.txt
cd ..

echo "... CO-2012-2010AG ..."
cd CO-2012-2010AG
analyze_plan.py CO-2012-2010AG-VPI-by-CD.csv CO-2012-2010AG-parms.txt
cd ..

echo "... CO-2012-2010G ..."
cd CO-2012-2010G
analyze_plan.py CO-2012-2010G-VPI-by-CD.csv CO-2012-2010G-parms.txt
cd ..

echo "... CO-2012-2010S ..."
cd CO-2012-2010S
analyze_plan.py CO-2012-2010S-VPI-by-CD.csv CO-2012-2010S-parms.txt
cd ..

echo "... CO-2012-2010SoS ..."
cd CO-2012-2010SoS
analyze_plan.py CO-2012-2010SoS-VPI-by-CD.csv CO-2012-2010SoS-parms.txt
cd ..

echo "... CO-2012-2012P ..."
cd CO-2012-2012P
analyze_plan.py CO-2012-2012P-VPI-by-CD.csv CO-2012-2012P-parms.txt
cd ..

END=$(date +"%T")
echo
echo "... finished @ $END."
echo
