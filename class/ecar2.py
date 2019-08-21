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

class Battery():
    def __init__(self,bsize=80):
        self.bsize=bsize

    def describe_battery(self):
        print("This car has a "+str(self.bsize)+"-kWh battery.")

class Ecar(Car):
    
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.bsize=Battery()

my_tesla=Ecar("tesla","model s",2018)
print(my_tesla.descriptive_name())
my_tesla.bsize.describe_battery()
