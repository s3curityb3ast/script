
# Importent Scripts for Pentesting...

* subdirb3r

``` 
A script useful for running dirb tool on the all enumerated subdomains for domain.
Usage:./subdirb3r.sh file-name-containing-domain-name-without-whitespace"

sample file 

cat a.txt
drive.google.com
mail.google.com
news.google.com
```

* cve2rating.py

```
A simple python script which shows the CVSS 2 and CVSS 3 Score on command line interface

Sample 

python cve2rating.py  CVE-2017-1337

('CVE Details for', 'CVE-2017-1337')
CVSS Score 3 for CVE-2017-1337
CVE score is: 
                                                8.1
                                            
Severity for is: High
 CVSS Score 2 for CVE-2017-1337
CVE score is: 
                                                4.3
                                            
Severity for is: MEDIUM

I am Looking for contribution for this tool,concept is pass the list of CVE ID's to the scirpt, like we pass ip list to nmap using iL flag. and expected output is below.

______________________________________________________________________
|CVE Details 	|	CVSS Score3 Score.       | CVSS Score2 Score     |
|				|            				 |				         |
|CVE-2017-1337 	|	Severity |  CVSS Score	 | Severity | CVSS Score |
|				|     High   |	8.1			 |	Medium  |      4.3   |           
|---------------------------------------------------------------------
 
```
Edits and pull request are always welcome... :)
S3curityB3ast
