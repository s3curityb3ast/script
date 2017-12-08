#!/usr/bin/python3
import requests                                                                                                                               
import os,sys,re
from bs4 import BeautifulSoup
cve = sys.argv[1]
print ('CVE Details for', (cve))
url = ('https://nvd.nist.gov/vuln/detail/')
page = requests.get((url)+(cve))
soup = BeautifulSoup(page.text, 'html.parser')


#For CVSS Score 3

print 'CVSS Score 3 for', (cve)
score = soup.find("div", {"id":"p_lt_WebPartZone1_zoneCenter_pageplaceholder_p_lt_WebPartZone1_zoneCenter_VulnerabilityDetail_VulnFormView_Vuln3CvssPanel"})
severity =  score.find('span')
sev = severity.get_text()
cvss3score =  score.find('a')
score = cvss3score.get_text()
print 'CVE score is:',(score)
print 'Severity for is:',(sev)

#for CVSS Score 2

print ' CVSS Score 2 for', (cve)
score = soup.find("div", {"id":"p_lt_WebPartZone1_zoneCenter_pageplaceholder_p_lt_WebPartZone1_zoneCenter_VulnerabilityDetail_VulnFormView_Vuln2CvssPanel"})
severity =  score.find('span')
sev = severity.get_text()
cvss3score =  score.find('a')
score = cvss3score.get_text()
print 'CVE score is:',(score)
print 'Severity for is:',(sev)
