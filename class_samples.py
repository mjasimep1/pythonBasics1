class MySampleClass:
    def hello(self,name):
        self.nm=name
    def setName(self):
        print("hi " + self.nm)
#MySampleClass().hello()
obj=MySampleClass()
obj.hello("Jasim")
obj.setName()
obj1=MySampleClass()
obj1.hello("John")
obj1.setName()