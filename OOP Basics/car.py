class Car:

    
    # constructor Method
    def __init__(self, make, model, year, color):
# Attributes (properries) than an object can have!

            self.make = make
            self.model = model
            self.year = year
            self.color = color
        
#Methods (Actions) that an object can do!
    def drive(self):
        print("This "+self.color+" car is driving")
    def stop(self):  
        print("This "+self.color+" car is stopped")