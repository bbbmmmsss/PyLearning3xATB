# Examples class, object ,constructors
class student:

    def __init__(self, name,marks):
        self.name = name
        # self.age = age
        self.marks = marks


    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi",self.name,"Your avg_marks is:",sum/3)


s1=student("Bhgayashree",[90,89,78])
s1.get_avg()