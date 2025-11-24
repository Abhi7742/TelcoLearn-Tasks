# slicing is used to asscessing parts of a string.

# str[starting index:ending index]   here the ending index is not included.



str = "hello this is siba"
    #  0123456789......
print(str[6])
print(str[3:13])
print(str[:8])    #[0:8]
print(str[1:len(str)])

# negative indexing is also possible
str2="welcome to python"
     #-9-8-7-6-5-4-3-2-1  
print(str2[-1])
print(str2[-3:])
print(str2[:-6])
print(str2[-len(str):-2])
 