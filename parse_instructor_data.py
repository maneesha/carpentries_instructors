import sys
import requests
from requests.auth import HTTPBasicAuth
import json

try:
    import local_settings

except:
    print("Local settings not found")
    sys.exit(1)

data = requests.get('https://amy.software-carpentry.org/api/v1/persons/?badges=2&badges=5&username=&personal=&middle=&family=&email=&may_contact=1&is_instructor=1&o=lastname', auth=HTTPBasicAuth(local_settings.user, local_settings.pw))

print(data.text)



