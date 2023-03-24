
class sampleConst:
    year=2020
    def __init__(self, name, age, place):
        self.name=name
        self.age=int(age)
        self.place=place

    def add_age(self):
        self.age=self.age+1

    def relocate(self,newPlace):
        self.place="Relocated to "+newPlace

    def displayAll(self):
        print("Name: "+self.name)
        print("Age: "+str(self.age))
        print("Place: "+self.place)
        print("year is: "+str(sampleConst.year))
        sampleConst.year=2021

obj=sampleConst("Jasim",30,"Calicut")
obj.displayAll()
obj.add_age()
obj.relocate("Ernakulam")
obj.displayAll()
print("main-year is : "+str(obj.year))
