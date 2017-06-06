# Inheritance
# Create a class called Mustang, that inherits from Car 
# and has an init function that only asks for year,
# and sets make = "Ford" and model = "Mustang"

class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model
    
    def age(self):
        return 2016 - self.year
        
        
class Mustang(Car):
    def __init__(self, year):
        self.year = year
        self.make = "Ford"
        self.model = "Mustang"
    
    
mustang1 = Mustang("2016")
print(mustang1)