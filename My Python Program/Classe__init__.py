class student:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=fname+lname+"@nitk.edu.in"


std1=student("Apoorv","Singh")
std2=student("Harsh","Singh")

print std1.email
print std2.email
