#Encaspulation
# outer sider can acces the inside method in encaspulation
# Encaspulation is nothing but wrapping the data
# In encaspulation privae fun is only private nothing can acces

class car:

    def __init__(self):
        self.public_var ="Public"
        self.__private_var="Private Car"
        self._protected_var="Protected Car"


    # def public_method(self):
    #     print("This is Public")

    def __private_method(self):
        print("This Private car")

    def PrintName(self):
        if self.__private_var=="Private Car":
            print("I am Private")
        print("I am Allowes in Public")


# This is end of class
alto = car()
alto.public_method="This is public"
alto.__private_method="This Private Car"
alto.PrintName()


