#!/bin/bash
TARGET=$1

cat $TARGET | while read line
do
   gobuster -u  https://$line/ -w /data/s3clist/Discovery/Web_Content/common.txt -o $line.txt -t 50 & 

done
