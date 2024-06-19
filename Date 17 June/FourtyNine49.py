# *args
# args is a special keyword which allows us to pass a variable number of arguments to a function.
# It is a tuple that contains the arguments passed to the function.
# args is nothing but a list

# Ex:1
def print_srguments(*args):
    for i in args:
        print(i, end=" ")


print_srguments("Vaibhav", "Meera")


# Ex:2
def new_arg(*args):
    for i in range(len(args)):
        print(args[i], end=" ")


new_arg("Vaibhav", "Meera", "Bhagyashree", "Rajat")


# Ex:3
def new_args(*args):
    for i in args:
        print(i)


new_args(5, 6, 7)
