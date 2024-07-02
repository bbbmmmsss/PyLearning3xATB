#Multiple Inhirantance
#    A     b
#     \     /
#     \   /
#      \ /
#       C
class Father:
    def Father_money(self):
        return 1000
        print("This is father mony")

class Mother:
    def Mother_money(self):
        return 5000
        print("This is mother mony")

class child(Mother,Father):
    pass
    # def self_money(self):
    #     print("This is child mony")

child1= child()
print(child1.Mother_money())
print(child1.Father_money())
# This is how child can access both father & mother money
