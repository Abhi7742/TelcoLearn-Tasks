# write a program to ask user to enter name of some sports and store them in a list.
sports=[]
sports.append(input("enter a sports: "))
sports.append(input("enter a sports: "))
sports.append(input("enter a sports: "))
print(sports)


# write a program to check if a list contains a palindrome of elements.

list=[1,2,3,4,3,2,1]
x=list.copy()
print(x)
x.reverse()
if(x==list):
    print("The list contains a palindrome.")
elif(x!=list):
    print("The list does not contain a palindrome.")


# write a program to reverse a string Sibaprasad sahoo to sahoo sibaprasad.

str="Sibaprasad sahoo"
x=str.split()
x.reverse()
print(x)
print(" ".join(x))