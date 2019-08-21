from collections import OrderedDict

fl=OrderedDict()

fl={"Kevin":["python","ruby"],"Harry":["C","Wolfram Language"],"Eva":["C","matlab","python"]}

for name,langlist in fl.items():
    print(name.title()+"'s fav languages are:")
    for lang in langlist:
        print("\t"+lang.title())
