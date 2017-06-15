should_continue = True
if should_continue == True:
	print("hello")


known_people = ['John', 'Anna', 'Mary']

person = input('Enter the person you know: ')

if person in known_people:
	print('You know {}'.format(person))
else:
	print("You don't know {}".format(person))

print(known_people)