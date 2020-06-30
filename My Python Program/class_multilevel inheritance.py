#multi-level Inheritance

class a:
    def pri(self):
        print "This is first"

class b(a):
    def pri1(self):
        print "This is derived from a"

class c(b):
    def pri2(self):
        print "This is derieved from b"



object1=c()
object1.pri()
object1.pri1()
object1.pri2()

