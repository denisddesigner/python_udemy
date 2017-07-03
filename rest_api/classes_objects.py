lottery_player_dict = {
	
	'name' : 'Rolf',
	'numbers' : (89, 34, 56, 3, 23)

}

print(sum(lottery_player_dict['numbers']))



class LotteryPlayer:
	def __init__(self, name):
		self.name = name
		self.numbers = (89, 34, 56, 3, 23)

	def total(self):
		return sum(self.numbers)

player_one = LotteryPlayer("Rolf") # creates an object from the class LotteryPlayer
player_two = LotteryPlayer("Denis")
player_one.numbers = (1, 23, 4, 54, 78)
print(player_one == player_two)
print(player_one.name)
print(player_two.name)
print(player_one.numbers)
print(player_two.numbers)
print(player_one.total())




##

class Student:
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []


	def average(self):
		return sum(self.marks) / len(self.marks)





anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(78)
print(anna.marks)
print(anna.average())
