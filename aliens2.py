#create a list names aliens
aliens=[]

#create 30 green aliens
for number in range(30):
    new_alien={"color":"green","points":5,"speed":"slow"}
    aliens.append(new_alien)

#show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#show the number of aliens we created
print(str(len(aliens))+" aliens were created.")
