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

# print(data.text)

# Pull just the persons records & transform to python dictionary
persons = json.loads(data.text)['results']


for person in persons[10:20]:
    print("PERSONAL NAME: ", person['personal'])
    print("FAMILY NAME: ", person['family'])
    print("EMAIL: ", person['email'])

    airport = person['airport'].split("/")[-2]
    print("AIRPORT: ", airport)
    
    print("WORKSHOPS AND ROLE: ")
    workshops = requests.get(person['tasks'], auth=HTTPBasicAuth(local_settings.user, local_settings.pw))
    workshops = json.loads(workshops.text)
    for workshop in workshops:
        print(workshop['event'].split("/")[-2], workshop['role'])

# person['tasks'] is a URL, will need to run requests on that to get all tasks

# Use loop not to print but to populate dictionary of all instructors

# Above code works for one page of API results. Will need to loop through to get all pages.
