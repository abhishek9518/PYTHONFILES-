
name=input("enter your name:")
print("Good Morning",name)
print("Good Morning" + name)

x = 5
y = 10
print(f"Sum of {x} and {y} is {x+y}")


name=input("enter your name:")
date=input("enter your date:")
print(f"\'''Dear {name},\n You are selected!\n {date}\'''")  

#OR 
my_name="Dear name,\n You are selected!\n date"
print(my_name.replace("name","abhishek").replace("date","19/11/2005"))
print(my_name)

#find double space 

my_string="This is a string with  double  spaces"
print(my_string.find("  ")) #finds the index of first double space