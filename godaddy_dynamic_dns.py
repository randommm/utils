#!/bin/python3

# Use a domain you have registed at Godaddy as dynamic dns for your computer
# Example: set subdomainname.domain.com as dynamic dns

import subprocess
import argparse

# You can get a key at https://developer.godaddy.com/
key="you_key_here"
secret="your_secret_here"

parser = argparse.ArgumentParser(description='Dynamic DNS on Godaddy')
parser.add_argument('--domain', dest='domain', #default='yourdomain.com',
                    help='Domain name.')
parser.add_argument('--subdomain', dest='subdomain', default='myapp',
                    help='Subomain name.')
parser.add_argument('--type', dest='type', default='A',
                    help='Record type.')
parser.add_argument('--delete', dest='delete', default=False, action='store_true',
                    help='Delete record instead of creating/updating it.')
parser.add_argument('--data', dest='data', default=None,
                    help='Data to pass to the record. Defaults to public IP.')
args = parser.parse_args()

data = args.data
if data is None:
     # Get external IP address Alternatives:
     # data='''curl https://4.ifcfg.me/ | tr -d "\r\n"'''
     # data='''external-ip | tr -d "\n"'''
     data = '''dig -4 TXT +short o-o.myaddr.l.google.com @ns1.google.com | awk -F'"' '{ print $2}' | tr -d "\r\n"'''
     data = subprocess.run(data, shell=True, capture_output=True).stdout.decode()

if args.delete:
     curl = f'''curl -X PUT -H "Authorization: sso-key {key}:{secret}" \
          -H "Content-Type: application/json" -H "Accept: application/json" \
          -d '[{{"data": "0.0.0.0", "ttl": 600}}]' \
          "https://api.godaddy.com/v1/domains/{args.domain}/records/{args.type}/{args.subdomain}"'''
     print(subprocess.run(curl, shell=True, capture_output=True).stdout.decode())
     print("record blanked")
else:
     curl = f'''curl -X PUT -H "Authorization: sso-key {key}:{secret}" \
          -H "Content-Type: application/json" -H "Accept: application/json" \
          -d '[{{"data":"{data}", "ttl": 600}}]' \
          "https://api.godaddy.com/v1/domains/{args.domain}/records/{args.type}/{args.subdomain}"'''
     print(subprocess.run(curl, shell=True, capture_output=True).stdout.decode())
     print("record registered")
