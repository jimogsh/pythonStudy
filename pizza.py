def pizza(*topping):
    print("The following toppings will be added:")
    for name in topping:
        print("- "+name)

pizza("a","b","c")
