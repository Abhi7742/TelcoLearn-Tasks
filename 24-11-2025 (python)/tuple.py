# tuples are used to store multiple items in a single variable.
# tuples are created using parentheses.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed.
# Once a tuple is created, you cannot change its values. 
# Tuples are unchangeable, or immutable .


tup=(1, 2, "hello", 4, 5,"hello")

print(tup)

print(type(tup))    

print(len(tup))      #print the length of the tuple

print(tup[2])        #get the item in tuple.


# single value tuples are always with , otherwise it will be considered as (int,float,string,boolean) etc.
test=(1,)
# test=("hello",)
print(test)
print(type(test))

