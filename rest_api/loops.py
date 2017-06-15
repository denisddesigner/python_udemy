my_variable = 'hello'

for char in my_variable: # iterables are strings, lists, sets, tuples etc.
	print(char)


count_down = True


while count_down == True:

	print(10)
	

	user_input = input("Should we count down again? (y/n)?")
	if user_input.lower() == 'n':
		count_down = False
	elif user_input.lower() == 'y':
		count_down = True
	else:
		print('Wrong input! Try Again!')
		input("Should we count down again? (y/n)?")

print('ALL DONE AT LAST!')