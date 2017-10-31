import parse_instructor_data
import jinja2
import send_util

url = 'https://amy.software-carpentry.org/api/v1/persons/?badges=2&badges=5&is_instructor=1&may_contact=1&o=lastname&page=1'

persons_data = parse_instructor_data.requests.get(url, auth=parse_instructor_data.HTTPBasicAuth(parse_instructor_data.local_settings.user, parse_instructor_data.local_settings.pw))

instructors = parse_instructor_data.create_instructor_dictionary(persons_data)

with open("email.txt") as fp:
    email_template = fp.read()

template = jinja2.Template(email_template)

for instructor in instructors:
    email_body = template.render(name=instructor['full name'], airport=instructor['airport'], workshops=instructor['workshops'] )

    #send_util.send_email(instructor['email'],'Please update your Software/Data Carpentry Instructor Information', email_body)
    print(email_body)
