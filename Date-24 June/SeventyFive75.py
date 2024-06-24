# Recursion
# Key case is: 1. Base case  2. Recursuve case

def factorial(n):
    if n==0:
        #base Case
        return 1
    # Recursive Case
    else:
     return n*factorial(n-1)
print(factorial(5))


