# Recursion Example:
def sum_of_digits(n):
    # Base Case
    if n<10:
        return n
    # Recursive case
    else:
        return n % 10 + sum_of_digits(n//10)

print(sum_of_digits((12345)))

# How recursion process are following
     # first get modules
     # & this modulud becomes next time in number for gets the values

number=12345
r1=number%10
s1=number//10     #(// gives quotient)
print(r1)
print(s1)

r2=s1%10
s2=s1//10
print(r2)
print(s2)

r3=s2%10
s3=s2//10
print(r3)
print(s3)

r4=s3%10
s4=s3//10
print(r4)
print(s4)

