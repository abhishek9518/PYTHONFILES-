# CONCEPT OF STINGS 
my_string = "ABHISHEK"
prt_string = my_string[0:8]
print(prt_string)

# slicing with step
print(my_string[0:8:2]) 

#FUNCTIONS OF STRINGS
my_string = "abhishek"
print(len(my_string)) # length of string

#ENDSWITH FUNCTION AND START WITH FUNCTION
my_string = "abhishek"
print(my_string.endswith("k")) # it will return true if string ends with k
print(my_string.startswith("a")) # it will return true if string starts with a
print(my_string.startswith("b")) # it will return false if string does not start with b
print(my_string.startswith("abhishek")) # it will return true if string starts with ab
 
