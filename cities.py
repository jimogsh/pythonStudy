prompt="Enter cities you have visited in the last year. Enter 'quit' to exit.\n"

while True:
    city=input(prompt)
    if city=="quit":
        break
    else:
        print(city)
