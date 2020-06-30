
#class library
class library:
    def __init__(self,booklist):
        self.booklist=booklist
    def display(self):
        print("Book list \n")
        for book in self.booklist:
            print book
    def borrowbook(self,bookname):
        if(bookname in self.booklist):
            print "Book is available."
            print "Take the book."
            self.booklist.remove(bookname)
        else:
            print "Book is not available"
    def returnbook(self,bookname):
        self.booklist.append(bookname)
    def addbook(self,bookname):
        self.booklist.append(bookname)


#class customer
class customer:
    def request(self):
        self.bookname= raw_input("Enter book name: ")
        return self.bookname
    def returnbook(self):
        self.bookname= raw_input("Enter book name: ")
        return self.bookname
        
        


lib=library(["Hindi","English","Punjabi"])
cus=customer()

while(1):
    print("*****Menu*****")
    print("1.Display Book")
    print("2.Request Book")
    print("3.Return Book")
    print("4.Add a Book (only for Manager)")
    print("5.Exit")
    choice=input("Enter a choice: ")
    if(choice==1):
        print("Diplay Book - List.")
        lib.display()
    elif(choice==2):
        a=cus.request()
        lib.borrowbook(a)
    elif(choice==3):
        a=cus.returnbook()
        lib.returnbook(a)
    elif(choice==4):
        print("Only one book can be added at a time.")
        a=raw_input("Enter Librarian Password: ")
        if(a=="12345"):
            a=raw_input("Enter book name: ")
            lib.addbook(a)
        else:
            print("Wrong Password.")
    elif(choice==5):
        exit()
    else:
        print("Wrong Choice.")
        
