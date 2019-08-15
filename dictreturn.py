def person(first,last,age=""):
    pp={"first":first,"last":last}
    if age:
        pp["age"]=age
    return pp

print(person("harry", "potter",25))
