unconfirmedUsers=["Alice","Bruce","Cindy"]
confirmedUsers=[]

while unconfirmedUsers:
    currentUser=unconfirmedUsers.pop()
    print("Verifying: "+currentUser.title()+".")
    confirmedUsers.append(currentUser)

print("The following users have been confirmed:")
for name in confirmedUsers:
    print(name.title())
