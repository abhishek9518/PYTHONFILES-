
collect = ["apple", "banana", "2", "2.33", "True",]
print(collect)
print(collect[0]) #accessing first element
print(collect[-1]) #accessing last element
collect[0] = "mango" #changing first element
print(collect)
print(collect[1:4]) #slicing
print(collect[1:]) #slicing from index 1 to end
print(collect[:4]) #slicing from start to index 4
print(collect[::2]) #slicing with step
print(collect[::-1]) #reversing the list
print(len(collect)) #length of list

for item in collect:
    print(item.capitalize()) #capitalize first letter of each element in list
    
collect.append(3)  
print(collect) #adding element at the end of list  



li1 = [1, 2, 3, 6, 5]
li1.sort()
print(li1) #sorting the list in ascending order

li1.reverse()
print(li1) #reversing the list

li1.insert(2, 4) #inserting element at index 2
print(li1)

li1.pop(2) #removing element at index 2
print(li1)  

li1.remove(5) #removing element 5 from list
print(li1)

#TUPLE
Tuple = (1, 2, 3, 4, 5) 
print(Tuple) #printing the tuple    
a=(1, 2, 3, 4, 5)
print(a)
a[0] = 10 #tuples are immutable, so this will give error

    
    
    
    
    