# Hangman

# 1. choose a word
# 2. assign number of guesses
# 3. guess - receive a letter from user
# 4. If letter in word print letter
# 5. Next guess
# 6. If not - print 'not in word' 
# 7. Decrease lives by 1 
# 8. Next letter
# 8. All letters found - Print 'You Won'
# 9. Lives < 0 - Print 'You Lost'


#################################################


# Solution


#################################################



import time


lives = 10
string_word = 'apple'
word = list('Apple'.lower())
guess = ["_"] * len(word)
winner = False
incorrectletters = []

# Print out current scoreboard
def printscore():
	print("\n\nLives: " + str(lives))
	print("Incorrect Letters: ", end="")
	for letter in range(len(incorrectletters)):
		if letter == len(incorrectletters) - 1:
			print(incorrectletters[letter], end="")
		else:
			print(incorrectletters[letter], end=",")
	print("")
	for letter in range(len(guess)):
		if letter == len(guess) - 1:
			print(guess[letter], end="")
		else:
			print(guess[letter], end="")
	print("")

# Ask the user for a letter
def askforletter():
	letterguess = input("Please guess a letter: ")
	correct = False
	for letter in range(len(word)):
		if letterguess == word[letter]:
			guess[letter] = letterguess
			correct = True

	if correct:
		print("You got one!")
	else:
		print("On no! That wasn't in there!")
		incorrectletters.append(letterguess)
		global lives 
		lives -= 1
	time.sleep(2)


# Check if they won
def checkwinner():
	if "_" not in guess:
		global winner
		winner = True




while lives > 0 and winner == False:
	
	
	

	# Print out current scoreboard
	printscore()

	# Ask the user for a letter
	askforletter()

	# Check if they won
	checkwinner()
	


if lives <= 0:
	print('You Lost! The word was ' + string_word)
else:
	print('Congratulations! You won with ' + str(lives) + ' lives left!')











































