def pmodels(unprinted,completed):
    while unprinted:
        currentmodel=unprinted.pop()
        print("Now printing: "+currentmodel)
        completed.append(currentmodel)
    print("\n")

def show_completed(completed):
    print("\nThe following models have been completed:")
    for name in completed:
        print(name)

unprinted=["model 1","model 2","model 3"]
completed=[]

pmodels(unprinted,completed)
show_completed(completed)
