Ex: 1


def new_function(a=9, b=4, c=2):
    return a + b + c


result = new_function()
result_1 = new_function(10, 20, )
result_2 = new_function(a=5, b=7, c=10)
print(result)
print(result_1)
print(result_2)

# OR we can print result in one line
print(result,result_1,result_2)

# So we can print n number of result in function
