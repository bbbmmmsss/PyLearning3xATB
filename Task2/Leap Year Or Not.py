# #Print 2024 leap year or not
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
year=int(input("Enter The Year:"))
if year %4 ==0 and year % 100 !=0:
    print(year," is leap year")
elif year%100==0:
    print(year,"is not leap year")
elif year%400==0:
    print(year, "is leap year")
else:
    print(year, "is not leap year")
