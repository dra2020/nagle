#!/bin/bash
#
# ANALYZE ALL STATES
#
# For example: 
#
# nagle_all.sh

START=$(date +"%T")

echo
echo "Starting to analyze all states @ $START ..."
echo

echo "... CA ..."
cd CA
analyze_CA.sh
cd ..

echo "... IL ..."
cd IL
analyze_IL.sh
cd ..

echo "... MA ..."
cd MA
analyze_MA.sh
cd ..

echo "... MD ..."
cd MD
analyze_MD.sh
cd ..

echo "... NC ..."
cd NC
analyze_NC.sh
cd ..

echo "... OH ..."
cd OH
analyze_OH.sh
cd ..

echo "... PA ..."
cd PA
analyze_PA.sh
cd ..

echo "... SC ..."
cd SC
analyze_SC.sh
cd ..

echo "... TN ..."
cd TN
analyze_TN.sh
cd ..

echo "... TX ..."
cd TX
analyze_TX.sh
cd ..

END=$(date +"%T")
echo
echo "... finished analyzing all states @ $END."
echo
