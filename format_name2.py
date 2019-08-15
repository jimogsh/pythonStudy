def formatname(first,last):
    fullname=first.title()+" "+last.title()
    return fullname

while True:
    fname=input("Please enter your first name, press 'q' to quit:\n")
    if fname=="q":
        break
    lname=input("Please enter your last name, press 'q' to quit:\n")
    if lname=="q":
        break
    print("Welcome, "+formatname(fname,lname)+"!")

