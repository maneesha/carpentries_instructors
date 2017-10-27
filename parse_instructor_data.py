import sys
import requests
from requests.auth import HTTPBasicAuth
import json

try:
    import local_settings

except:
    print("Local settings not found")
    sys.exit(1)


def create_instructor_dictionary(data):
# Pull just the persons records & transform to python dictionary
    persons = json.loads(data.text)['results']

    instructors = []

    for person in persons:
        d = {}

        if person['airport']:
            airport = person['airport'].split("/")[-2]
        else:
            airport = "unknown"
            
        workshops = requests.get(person['tasks'], auth=HTTPBasicAuth(local_settings.user, local_settings.pw))
        workshops = json.loads(workshops.text)
        workshops_list = []
        for workshop in workshops:
            workshops_list.append(workshop['event'].split("/")[-2] + " " + workshop['role'])


        badges = requests.get(person['awards'], auth=HTTPBasicAuth(local_settings.user, local_settings.pw))
        badges = json.loads(badges.text)
        badges_list = []
        for badge in badges:
            # print(badge['badge'], badge['awarded'])
            badges_list.append(badge['badge'] + ' awarded on ' + badge['awarded'])

        d['full name'] = person['personal'] + " " +  person['family']
        d['email'] = person['email']
        d['airport'] = airport
        d['workshops'] = workshops_list
        d['badges'] = badges_list

        instructors.append(d)

    return instructors

# Above code works for one page of API results. Will need to loop through to get all pages.
