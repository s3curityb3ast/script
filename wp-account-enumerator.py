#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import json
import urllib.request

if len(sys.argv) < 2:
    print("Usage: ./wp-account-enumerator.py <domain>")
    sys.exit()

print('Enumerating account info for {}'.format(sys.argv[1]))

try:
    o = urllib.request.build_opener()
    o.addheaders = [('User-Agent','Mozilla/5.0')]
    with o.open(sys.argv[1] + '/wp-json/wp/v2/users') as f:
        j = json.loads(f.read().decode('utf-8'))
    print('\n'.join(u['name'] for u in j))

except:
    print("Oops, something goes wrong!")
