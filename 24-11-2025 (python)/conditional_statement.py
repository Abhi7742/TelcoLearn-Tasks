'''if(condition):
    statement1
elif(condition)
    statement2
else:'''
    
a=int(input("enter a number: "))
if(a==0):
    print("you entered zero")
elif(a%2==0):
    print("even")
else:
    print("odd")    


mark=int(input("enter the mark: "))
if(mark>=90):
    print("A+")
elif(mark>=80 and mark<90):
    print("A")
elif(mark>=70 and mark<80):
    print("B")
elif(mark>=60 and mark<70):
    print("C")
else:
    print("F")
