def find_even_odd(num):
    if num %2==0:
        print("even")
    else:
        print("odd")

find_even_odd(3)

even_odd =lambda num:"even" if num % 2==0 else "odd"
print(even_odd(4))