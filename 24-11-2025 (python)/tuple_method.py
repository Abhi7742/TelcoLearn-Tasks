tup=(1,2,3,4,3,2,1)

print(tup.index(3))         #it returns index of first occurance.

print(tup.count(3))        # count total occurance of the element.


# directly you can't change the value of tuple
student=("siba","manas","rahul","badal")
student1=list(student)
student1[2]="rohan"
student=tuple(student1)

print(student)
print(type(student))


# in Python, we are also allowed to extract the values back into variables. This is called "unpacking".

fruits=("cherry","apple","orange","guava")
(yellow,red,purple,black)=fruits
print(black)
