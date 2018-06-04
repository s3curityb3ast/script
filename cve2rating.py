#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import requests
from bs4 import BeautifulSoup

def logger(f,s):
    print(s,end='')
    f.write(s)

if len(sys.argv) < 2:
    print('Usage: cve2rating.py <file>')
    sys.exit()

with open(sys.argv[1],'r') as fin:
    cves = fin.read().splitlines()

try:
    fout = open('result.txt','a')

    for cve in cves:
        page = requests.get('https://nvd.nist.gov/vuln/detail/' + cve)
        soup = BeautifulSoup(page.text, 'html.parser')
        logger(fout, 'CVE details for: {}\n'.format(cve))

        try:
            scr = soup.find('span',attrs={u'data-testid': u'vuln-cvssv3-base-score'}).get_text().strip()
            sev = soup.find('span',attrs={u'data-testid': u'vuln-cvssv3-base-score-severity'}).get_text().strip()
            exp = soup.find('span',attrs={u'data-testid': u'vuln-cvssv3-exploitability-score'}).get_text().strip()
            logger(fout, 'CVSS3 score: {}\nCVSS3 severity: {}\nCVSS3 Exploitability: {}\n'.format(scr,sev,exp))

        except AttributeError:
            print('Oops..! CVSS3 not found in the database')

        try:
            scr = soup.find('span',attrs={u'data-testid': u'vuln-cvssv2-base-score'}).get_text().strip()
            sev = soup.find('span',attrs={u'data-testid': u'vuln-cvssv2-base-score-severity'}).get_text().strip()
            logger(fout, 'CVSS2 score: {}\nCVSS2 severity: {}\n\n'.format(scr,sev))

        except AttributeError:
            print('Oops..! CVSS2 not found in the database')

except KeyboardInterrupt:
    print("User interrupt!")

finally:
    fout.close()
