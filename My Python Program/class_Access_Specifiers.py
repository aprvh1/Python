class apoorv:
    a=10
    _b=20
    __c=30


class ape(apoorv):
    def pri(self):
        print "b: ",self._b    #This _b will work and b will give error
        print "b: ",self._apoorv__c
        

t=ape()
print"t: ",t.a
t.pri()

t1=apoorv()
print"t: ",t1._apoorv__c    #_apoorv -> This is addition
