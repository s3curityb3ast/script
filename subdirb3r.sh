#!/bin/bash
# sample file which contain domain name
# google.com
# g.co
# drive.google.com

echo "dirb enumrator for subdomain by @S3curityb3ast"

if [[ "$1" == "" ]]; then
    echo "usage ./subdirb3r.sh file-name-containing domain name without whitespace"
    exit
fi

while read line; do
    dirb https://$line/ -f -o $line.txt &
done < $1
