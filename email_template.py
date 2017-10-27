import parse_instructor_data

persons_data = parse_instructor_data.requests.get('https://amy.software-carpentry.org/api/v1/persons/?badges=2&badges=5&username=&personal=&middle=&family=&email=&may_contact=1&is_instructor=1&o=lastname', auth=parse_instructor_data.HTTPBasicAuth(parse_instructor_data.local_settings.user, parse_instructor_data.local_settings.pw))

instructors = parse_instructor_data.create_instructor_dictionary(persons_data)

