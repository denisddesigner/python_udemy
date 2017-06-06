'''
try:
	birthyear = int(input('What year were you born? '))
	print("You were born in " + str(birthyear))
except Exception:
	print('Number please, you bonehead!')


def love():
	print('I love Python')

love()


word = "first"

def firstletter(string):
    
    print(string[0])
    
firstletter(word)

'''


teams = ['Madrid', 'Barcelona', 'United']
print(teams)
teams.insert(1, 'Arsenal')
print(teams)
teams[2] = 'Bayern'
print(teams)
del(teams[2])
print(teams)
teams.remove('United')
print(teams)
print(len(teams))


# sets

teams2 = set(['Madrid', 'Barcelona', 'United', 'United'])
print(teams2)
teams2.add('Ajax')
print(teams2)
teams2.remove('Barcelona')
print(teams2)
teams2.discard('Barca') # discard removes but no error with misspelling
print(teams2)
