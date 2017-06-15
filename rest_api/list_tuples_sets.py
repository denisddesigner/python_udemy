grades = [54, 65, 67, 89, 90] # lists are the most versatile, and they ordered
print(grades)
grades.append(108)
print(grades)

print(sum(grades) / len(grades))




tuple_grades = (54, 65, 67, 89, 90) # tuple is immutable
print(tuple_grades)

tuple_grades = tuple_grades + (100,)
print(tuple_grades)


set_grades = {54, 65, 67, 89, 90, 90} # unique and unordered
set_grades.add(60)
print(set_grades)

## Set Operations
your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

print(your_lottery_numbers.intersection(winning_numbers))
print(your_lottery_numbers.union(winning_numbers))
print({1, 2, 3, 4}.difference({1,2}))


my_list = [1, 2, 3]
list2= [1, 2, 2, 3]
print(sum(my_list))
print(sum(list2))
