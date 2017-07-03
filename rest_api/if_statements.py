'''should_continue = True
if should_continue == True:
	print("hello")


known_people = ['John', 'Anna', 'Mary']

person = input('Enter the person you know: ')

if person in known_people:
	print('You know {}'.format(person))
else:
	print("You don't know {}".format(person))

print(known_people)'''


## Exercise

def who_do_you_know():
	# Ask the user for a list of people they know
	# Split the string into a list
	people = input("A list of people you know please: ")
	
	people_without_spaces = [person.strip() for person in people.split(",")]

	return people_without_spaces




def ask_user():
	# Ask user for a name
	# See if the name is in the list of people they know
	# Print out that they know the person
	person = input("Name of a person please: ")
	if person in who_do_you_know():
		print("You know {}".format(person))

ask_user()





