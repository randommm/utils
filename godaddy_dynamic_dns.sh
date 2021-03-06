#!/bin/bash

#Use a domain you have registed at Godaddy as dynamic dns for your computer
#Example: set subdomainname.domain.com as dynamic dns
#Optional argument delete or del to set subdomain to 0.0.0.0

#You can get a key at https://developer.godaddy.com/

key="you_key_here"
secret="your_secret_here"
domain="domain.com"
subdomain="subdomainname"

if [ "x$@" = "x" ]
then
curl -X PUT -H "Authorization: sso-key ${key}:${secret}" \
     -H "Content-Type: application/json" -H "Accept: application/json" \
     -d "[{\"data\":\"`external-ip | tr -d "\n"`\", \"ttl\": 600}]" \
     "https://api.godaddy.com/v1/domains/${domain}/records/A/${subdomain}"
elif [ $@ = "delete" ] || [ $@ = "del" ]
then
#there does not seem to be possible to easily delete a record
#so we just set it to 0.0.0.0
curl -X PUT -H "Authorization: sso-key ${key}:${secret}" \
     -H "Content-Type: application/json" -H "Accept: application/json" \
     -d "[{\"data\": \"0.0.0.0\"}]" \
     "https://api.godaddy.com/v1/domains/${domain}/records/A/${subdomain}"
else
echo "Unrecognized argument" 1>&2
exit 1
fi

