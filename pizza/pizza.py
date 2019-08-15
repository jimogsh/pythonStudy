def pizza(size,*topping):
    print("Make a "+str(size)+"-inch pizza with:")
    for name in topping:
        print("- "+name)

