def PreExistingBooks():
    return l
l,l2=[],[]
l1=PreExistingBooks()
import pickle
class Books:
    
    def __init__(self,bname,isbn,bauthor):
        self.bname=bname
        self.isbn=isbn
        self.bauthor=bauthor
        d={}
        l=[self.isbn,self.bauthor]
        d[self.bname]=l
        l1.append(d)
        with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/Books.pkl", 'ab') as f:
            pickle.dump(d,f)
        print("Book Added Successfully")
def LoadBooks():
    with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/pwd.dat","rb") as f:
        while True:
            try:
                obj=pickle.load(f)
                l2.apppend(obj)
            except Exception:
                break
    if len(l2)==0:
        b1={"C":['1000','Yashwant Kanetkar']}
        b2={"C++":['1001','Sumita Arora']}
        b3={"Mastering Java":['1003','J.K. Rowling']}
        b4={"P For Python":['1004','Timothy Olyphant']}
        b5={"Data Structures":['1005','Greg Kinnear']}
        b6={"Suburban Tradegy":['1006','Sidney hall']}
        l1=[b1,b2,b3,b4,b5,b6]
        with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/Books.pkl","wb") as f:
            pickle.dump(b1,f)
            pickle.dump(b2,f)
            pickle.dump(b3,f)
            pickle.dump(b4,f)
            pickle.dump(b5,f)
            pickle.dump(b6,f)
def PreExistingBooks():
    return l