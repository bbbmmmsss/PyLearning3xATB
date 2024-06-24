#To find a key in dictonary
dict={'a':6,'b':8,'c':4}
op='a' in dict
print(op)

# Another Way to find  a key in dictonary
print('a' in dict)

# Another way by using for loop
for i in dict.keys():
    if i=='a':
        print("a present in my dictonary")
        break