import parse_instructor_data
import jinja2

# This whole thing needs to be in a loop to go through all 12 pages of API

page_number = 1

url = 'https://amy.software-carpentry.org/api/v1/persons/?badges=2&badges=5&is_instructor=1&may_contact=1&o=lastname&page=' + str(page_number)

persons_data = parse_instructor_data.requests.get(url, auth=parse_instructor_data.HTTPBasicAuth(parse_instructor_data.local_settings.user, parse_instructor_data.local_settings.pw))

instructors = parse_instructor_data.create_instructor_dictionary(persons_data)

with open("email.txt") as fp:
    email_template = fp.read()

template = jinja2.Template(email_template)

for instructor in instructors:
    
    email_body = template.render(name=instructor['full name'], airport=instructor['airport'], workshops=instructor['workshops'], badges=instructor['badges'] )

    print(email_body)
