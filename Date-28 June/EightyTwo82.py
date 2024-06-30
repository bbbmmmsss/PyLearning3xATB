# Enaxaspulation is means security
class MyClass:

    def __init__(self):
        self.name="Bhagyashree"

    def Public_function(self):
        print("This is a public function")

    def __Private_function(self):
        print("This is a private function")

    def public_fn__private(self):
        self.__Private_function()


a= MyClass()
a.Public_function()
a.public_fn__private()
