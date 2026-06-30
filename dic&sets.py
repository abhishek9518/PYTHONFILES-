# DICTIONARY 
marks = {"maths": 90, "science": 80, "english": 70}

print(marks)
print(marks["maths"])
print(type(marks)) 
print(marks.keys())
print(marks.values())
print(marks.items())
print(marks.get("science"))
print(marks.get("social", "not"))
marks.update({"social": 60})
print(marks)


#SETS 
a = {1, 2, 3, 4, 5}
a.add(6)
print(a)
b = a.union({7, 8, 9})
print(b)



