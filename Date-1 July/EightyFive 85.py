#Inhritance----------------
# There are 6 Types of inritance:
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance


#1. Single Inhritance--------------------------------
class GrandParent:
    key=10
    def GrandParant_method(self):
        return "This function is in GrandParentparent class."

class Parent(GrandParent):
    def parent_method(self):
       return "This function is in Parent class."

GrandParant=Parent()
print(GrandParant.parent_method())   #Call Parent class method
print(GrandParant.GrandParant_method())   #Call GrandParent class method
print(Parent.GrandParant_method)   # We can not call grandparent class method by using parent class object
print(Parent.key)    #10