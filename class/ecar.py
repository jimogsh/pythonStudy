class Car():

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0

    def descriptive_name(self):
        fullname=str(self.year)+" "+self.make+" "+self.model
        return fullname.title()
    def updateodometer(self,milage):
        if milage>=self.odometer:
            self.odometer=milage
        else:
            print("Warning!")
    def readtheodometer(self):
        print("This car has "+str(self.odometer)+" miles on it.")

class Ecar(Car):
    
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=70

    def describe_battery_size(self):
        print("This electric car has a "+str(self.battery_size)+"-kWh battery.")

my_tesla=Ecar("tesla","model s",2018)
print(my_tesla.descriptive_name())
my_tesla.describe_battery_size()
