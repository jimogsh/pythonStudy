prompt="\nTell me something here:"
prompt+="\nThe program will quit if you enter 'quit'\n"
message=''

while message!="quit":
    message=input(prompt)
    if message!="quit":
        print(message)
