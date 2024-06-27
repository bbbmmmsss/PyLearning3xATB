#Class & Object

class calc:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def mod(self, a, b):
        return a % b

    def __init__(self):
        print("Calculator")


calculate = calc()
output = calculate.sum(10, 20)
print(output)
