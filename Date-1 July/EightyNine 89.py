#Hybrid Inheritance
#       A
#     /   \
#    B     C
#    \    |
#      D


class A:
    def func(self):
        print("Function inside A")

class B(A):
    def func1(self):
        print("Function inside B")

class C(A):
    def func2(self):
        print("Function inside C")

class D(B,C):
    def func3(self):
        print("Function inside D")

d=D()
print(d.func())
print(d.func1())
print(d.func2())
print(d.func3())