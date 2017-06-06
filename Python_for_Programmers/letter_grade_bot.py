# Letter Grade Bot
studentName = input("Student Name: ")

def calculate_grade():

	percentage = score * 100 / pointspossible
	grade = ""

	if 100 >= percentage >= 90:
		grade = 'A'
	elif 89 >= percentage >= 80:
		grade = 'B'
	elif 79 >= percentage >= 70:
		grade = 'C'
	elif 69 >= percentage >= 60:
		grade = 'D'
	else:
		grade = 'F'
	# Print the student name and what grade they got
	print('Percentage: {}'.format(percentage))
	print('{}:{}'.format(studentName, grade))

try:
	pointspossible = int(input("Maximum Score: "))
	score = int(input("Student Score: "))
	calculate_grade()
	

except Exception:
	print("You need to input a number!")

	














