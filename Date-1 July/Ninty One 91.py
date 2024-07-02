#Method Overriding
# Method overriding is a run time polymorphism in which a subclass or child class overrides a method defined in the parent class.

class Animal:
    def speak(self):
        print("The animal speaks")

    def Bark(self):
        print("The Dog barks")

class Dog(Animal):
    def speak(self):
        print("The Dog barks")

    def Bark(self):
        print("The Dog barks")

class Cat(Animal):
    def speak(self):
        print("The Cat Meows")

    def Meow(self):
        print("The Cat Meows")

obj=Animal()
obj.speak()
obj_dog=Dog()
obj_dog.speak()