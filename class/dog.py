class Dog():

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(self.name.title()+" is sitting.")

    def roll(self):
        print(self.name.title()+" rolled over.")

mydog=Dog("Willie",3)
print("My dog's name is "+mydog.name.title()+".")
