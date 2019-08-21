class Car():

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0

    def descriptive_name(self):
        fullname=str(self.year)+" "+self.make+" "+self.model
        return fullname.title()
    def readtheodometer(self):
        print("This car has "+str(self.odometer)+" miles on it.")     
    def updateodometer(self,milage):
        if milage>=self.odometer:
            self.odometer=milage
        else:
            print("Warning!")
    def incrementodometer(self,miles):
        self.odometer+=miles

class Battery():

    def __init__(self,battery_size=70):
        self.battery_size=battery_size

    def descriptive_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery.")

    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=370
        print("This car can go approximately "+str(range)+" miles on a full charge.")

class ElectricCar(Car):
    
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
