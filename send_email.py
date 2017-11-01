import parse_instructor_data
import jinja2
import send_util

# This whole thing needs to be in a loop to go through all 12 pages of API

for page in range(1,13):
    print("Now on page " + str(page))
    url = 'https://amy.software-carpentry.org/api/v1/persons/?badges=2&badges=5&is_instructor=1&may_contact=1&o=lastname&page=' + str(page)
    persons_data = parse_instructor_data.s.get(url)
    instructors = parse_instructor_data.create_instructor_dictionary(persons_data)

    with open("email.txt") as fp:
        email_template = fp.read()

    template = jinja2.Template(email_template)

    for instructor in instructors:

        email_body = template.render(name=instructor['full name'], airport=instructor['airport'], workshops=instructor['workshops'], badges=instructor['badges'] )

        #send_util.send_email('jonah@duckles.org','Please update your Software/Data Carpentry Instructor Information', email_body)
        try:
            print("Sent to " + instructor['email'])
            send_util.send_email(instructor['email'],'Please update your Software/Data Carpentry Instructor Information', email_body)
        except:
            print("missing email address")
