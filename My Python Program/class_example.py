class Myclass:
    count=0
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
        Myclass.count+=1         #nameofclass.count+=1


    def print1(self):
        print "Name: ",self.name
        print "Salary: ",self.sal

emp1 = Myclass("Apoorv",10)
emp2 = Myclass("Harsh",20)
emp3 = Myclass("Aman",30)
emp4 = Myclass("Ladoo",40)



emp1.print1()
emp2.print1()
emp3.print1()
emp4.print1()


print "No of Employees: ",Myclass.count

