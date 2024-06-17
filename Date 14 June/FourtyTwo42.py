# Write a program by using switch case in string char

Browser= str(input("Enter The Browser name:"))
match Browser:
    case "Chrome":
        print("Chrome is Running")
    case "Edge":
        print("Edge is Running")
    case _:
        print("Invalid Browser")