class apoorv:
    def __init__(self):
        print "This is my base class"
    def take(self,name):
        self.name=name
    def printname(self):
        print "NAME: ",self.name


class ape(apoorv):
    def __init__(self):
        print "This is my derieved class"
        
    
a=ape()
a.take("Aman")
a.printname()
