#Abstraction
# In abstraction hide the internal implementation of the function and only show the functionality

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod   # Abstract means is incomplete method
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("The Dog barks")

class Cat(Animal):
    def speak(self):
        print("The Cat Meows")


dog=Dog()
print(dog.speak())

cat=Cat()
print(cat.speak())