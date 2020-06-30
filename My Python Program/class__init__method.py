class apoorv:
    "This is my class"
    def __init__(self):
        print "This is my constructor"
    def print1(self,name):
        print "Hello ",name

a=apoorv()
a.print1("Apoorv")

print a.__doc__
