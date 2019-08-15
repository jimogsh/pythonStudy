alien={"x_position":0, "y_position":25, "speed":"medium"}
print("Original x-position "+ str(alien["x_position"])+".")

# Speed levels
if alien["speed"]=="slow":
    x_increment=1
elif alien["speed"]=="medium":
    x_increment=2
else:
    x_increment=3

alien["x_position"]+=x_increment
print("New x_position "+ str(alien["x_position"]))
