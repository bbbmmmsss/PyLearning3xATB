#Factorial of number
import math

n=5
factorial=1
# math.factorial(n)

for i in range(1,n+1):
    factorial = factorial * i
print(factorial)

# 5*4*3*2*1=120