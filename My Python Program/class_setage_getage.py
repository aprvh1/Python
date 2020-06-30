class apoorv:
    def setage(self,age):
        self.ageofclass=age

    def getage(self):
        return self.ageofclass



a=apoorv()
a.setage(22)
print a.getage()

a.setage("Twenty one")
print a.getage()
