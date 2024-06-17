# We can check multiple number name ,input by using match case/Switch case
def allow_to_enter_the_class(name):
    match name:
        case "Bhagyashree":
            print("You are allowed to enter the class")
        case "Ravi":
            print("You are allowed to enter the class")
        case "Mahesh":
            print("You are allowed to enter the class")
        case _:
            print("You are not allowed to enter the class")
allow_to_enter_the_class("Bhagyashree")
allow_to_enter_the_class("Mohini")

# check a function by using if else condition
def  check_function(name):
    if name == "Bhagyashree":
        print("You are allowed to enter the class")
    elif name == "Ravi":
        print("You are allowed to enter the class")
    elif name == "Mahesh":
        print("You are allowed to enter the class")
    else:
        print("You are not allowed to enter the class")
check_function("Bhagyashree")