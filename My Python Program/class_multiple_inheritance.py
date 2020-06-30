class apoorv:
    def __init__(self):
        print "This is my base class"
    def take(self,name):
        self.name=name
    def printname(self):
        print "NAME: ",self.name

class apoo:
    web="www.flipkart.com"
    name="Flipkart"

    def printthings(self):
        print "Website: ",self.web

class ape(apoo,apoorv):
    def __init__(self):
        print "This is my derieved class"

    def printname(self):
        print "This is name: ",self.name
        
    
a=ape()
a.take("Aman" ) #as this method is of class apoorv, if it is derieved second also if we class printname() method it will be executed of apoorv class only.
a.printname()
