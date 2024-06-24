#Filter
# The Filter() function in python is a built in function that allows you to filter a list or other iterable object.
# It takes a function as an argument and returns an iterator.
# Filter function returns True or false
# Map function returns numbers
number=[1,2,3,4,5,6,7,8,9,10]
def is_even(number):
    return number % 2 == 0

print(list(filter(is_even, number)))

# Another method s(hort)

num=[1,2,3,4,5,6,7,8,9]
def greater_than_5(num):
    return num>5

greater_number=filter(greater_than_5,num)
print(list(greater_number))
