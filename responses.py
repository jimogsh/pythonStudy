responses={}

active=True

while active:
    name=input("What's your name?")
    response=input("Which city do your visited recently?")
    responses[name]=response
    repeat=input("Do you want someone more to do this response?(yes/no)")
    if repeat=="no":
        active=False

#print(responses)
print("Results:")
for name,response in responses.items():
    print(name.title()+" has just visited "+response.title()+".")
