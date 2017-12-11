#!/bin/bash 

touch result.txt	#create a new file for saving result

TARGET=$1		#treat first argument as an input

cat $TARGET | while read line #run the loop for multiple CVES
do
   python cve2rating.py  $line  >> result.txt  

done
