#MultiLevel Inhritance
# A(GrandParent)
# |
# B(Parent)
# |
# C(Son)

class A:
    def a(self):
        print("A")

class B(A):
    def b(self):
        print("B")

class C(B):
    def c(self):
        print("C")

B_obj=B()
print(B_obj.b())
print(B_obj.a())

