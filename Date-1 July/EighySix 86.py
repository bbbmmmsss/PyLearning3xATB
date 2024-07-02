# Hierarchical Inhritance------------
# One parent and this parent have multiple childerns
#                   A         ----------------Parent
#                /  |  \
#              B    C   D     ----------------Multiple Childerns


class Father:
    def BHK1(self):
        print("This is BHK1")

class Son1:
    def BHK2(self):
        print("This is BHK2")

class Son2:
    def BHK3(self):
        print("This is BHK3")

son_1=Son1()
son_1.BHK2()


son_2=Son2()
son_2.BHK3()


