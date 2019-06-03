#!/bin/bash
#
# ANALYZE A BATCH OF PLANS
#
# For example: 
#
# analyze_OH.sh

START=$(date +"%T")

echo
echo "Started analyzing plans @ $START ..."
echo

echo "... OH-2012-2004P ..."
cd OH-2012-2004P
analyze_plan.py OH-2012-2004P-VPI-by-CD.csv OH-2012-2004P-parms.txt
cd ..

echo "... OH-2012-2006A ..."
cd OH-2012-2006A
analyze_plan.py OH-2012-2006A-VPI-by-CD.csv OH-2012-2006A-parms.txt
cd ..

echo "... OH-2012-2006AG ..."
cd OH-2012-2006AG
analyze_plan.py OH-2012-2006AG-VPI-by-CD.csv OH-2012-2006AG-parms.txt
cd ..

echo "... OH-2012-2006G ..."
cd OH-2012-2006G
analyze_plan.py OH-2012-2006G-VPI-by-CD.csv OH-2012-2006G-parms.txt
cd ..

echo "... OH-2012-2006S ..."
cd OH-2012-2006S
analyze_plan.py OH-2012-2006S-VPI-by-CD.csv OH-2012-2006S-parms.txt
cd ..

echo "... OH-2012-2006SoS ..."
cd OH-2012-2006SoS
analyze_plan.py OH-2012-2006SoS-VPI-by-CD.csv OH-2012-2006SoS-parms.txt
cd ..

echo "... OH-2012-2006T ..."
cd OH-2012-2006T
analyze_plan.py OH-2012-2006T-VPI-by-CD.csv OH-2012-2006T-parms.txt
cd ..

echo "... OH-2012-2008AG ..."
cd OH-2012-2008AG
analyze_plan.py OH-2012-2008AG-VPI-by-CD.csv OH-2012-2008AG-parms.txt
cd ..

echo "... OH-2012-2008P ..."
cd OH-2012-2008P
analyze_plan.py OH-2012-2008P-VPI-by-CD.csv OH-2012-2008P-parms.txt
cd ..

echo "... OH-2012-2010-12D ..."
cd OH-2012-2010-12D
analyze_plan.py OH-2012-2010-12D-VPI-by-CD.csv OH-2012-2010-12D-parms.txt
cd ..

echo "... OH-2012-2010A ..."
cd OH-2012-2010A
analyze_plan.py OH-2012-2010A-VPI-by-CD.csv OH-2012-2010A-parms.txt
cd ..

echo "... OH-2012-2010AG ..."
cd OH-2012-2010AG
analyze_plan.py OH-2012-2010AG-VPI-by-CD.csv OH-2012-2010AG-parms.txt
cd ..

echo "... OH-2012-2010G ..."
cd OH-2012-2010G
analyze_plan.py OH-2012-2010G-VPI-by-CD.csv OH-2012-2010G-parms.txt
cd ..

echo "... OH-2012-2010S ..."
cd OH-2012-2010S
analyze_plan.py OH-2012-2010S-VPI-by-CD.csv OH-2012-2010S-parms.txt
cd ..

echo "... OH-2012-2010SoS ..."
cd OH-2012-2010SoS
analyze_plan.py OH-2012-2010SoS-VPI-by-CD.csv OH-2012-2010SoS-parms.txt
cd ..

echo "... OH-2012-2010T ..."
cd OH-2012-2010T
analyze_plan.py OH-2012-2010T-VPI-by-CD.csv OH-2012-2010T-parms.txt
cd ..

echo "... OH-2012-2012P ..."
cd OH-2012-2012P
analyze_plan.py OH-2012-2012P-VPI-by-CD.csv OH-2012-2012P-parms.txt
cd ..

echo "... OH-2012-2012S ..."
cd OH-2012-2012S
analyze_plan.py OH-2012-2012S-VPI-by-CD.csv OH-2012-2012S-parms.txt
cd ..

END=$(date +"%T")
echo
echo "... finished @ $END."
echo
