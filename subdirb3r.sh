#!/bin/bash

echo "dirb enumrator for subdomain by  @S3curityb3ast"
echo "usage ./subdirb3r.sh file-name-containing domain name without whitespace"

TARGET=$1

cat $TARGET | while read line
do
   dirb https://$line/ -f -o $line.txt & 

done

#sample file which contain domain name
#google.com
#g.co
#drive.google.com
