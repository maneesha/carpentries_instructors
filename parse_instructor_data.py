import sys
import requests
from requests.auth import HTTPBasicAuth

try:
    import local_settings

except:
    print("Local settings not found")
    sys.exit(1)

data = requests.get('https://amy.software-carpentry.org/api/v1/persons/?format=json', auth=HTTPBasicAuth(local_settings.user, local_settings.pw))


print(data.text)
