class car:
    name=None
    make=None
    model=None

    def __init__(self,o_name,o_make,o_model):
        self.name=o_name
        self.make=o_make
        self.model=o_model

    def start_engine(self):
        print("Car name is:"+self.name)
        print("Car make is: "+self.make)
        print("Car Model is: "+self.model)

lambo=car("Aventador","Lamborghini","2019")
print(lambo.start_engine())