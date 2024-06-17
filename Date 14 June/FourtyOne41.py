#Multiple Condition (by using switch condition)
numbers=int(input("Enter the Number: "))
match numbers:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid Number")

# We can use match for character /string
char=input("Enter the Character: ")
match char:
    case 'A':
        print("Character A Printed")
    case 'B':
            print("Character B Printed")
    case 'c':
            print("Character C Printed")
    case _:
            print("Invalid Character")
