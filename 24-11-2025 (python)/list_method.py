fruits=["apple", "banana", "cherry", "mango", "orange", "pepper","cherry"]
       #   0,        1,        2,       3,          4,      5.
bikes=["MT","KTM","RE","HERO"]
print(fruits)

fruits.append("guava")         # it will append the guava at the end of the list.
print(fruits)

fruits.insert(2, "grape")       # insert method is used to add an element at the specified position.
print(fruits)

fruits.sort()
print(fruits)                 #sorts in ascending order(1,2,3) 

fruits.sort(reverse=True)       #sorts in descending order(3,2,1)
print(fruits)

fruits.reverse()                #reverses the list as it is.
print(fruits)

fruits.remove("cherry")        #it remove the first occurance of element in the list.
print(fruits)

fruits.pop(2)                  #it remove the element at the specified index.
print(fruits)

foods=fruits.copy()            #it will copy the list to another.
print(foods)

# Both the methods are same for join two lists.
list=bikes+fruits
print(list)

bikes.extend(fruits)
print(bikes)

bikes.clear()                 #remove all the elements from the list bike.
print(bikes)
