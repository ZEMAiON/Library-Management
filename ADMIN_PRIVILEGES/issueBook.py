import time,pickle
l=[]
def issueBook(n1,rollno):
     with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/IssueBooks.pkl","ab") as f:
        d={}
        l1=[]
        sec=time.time()
        l1.append(n1)
        l1.append(sec)
        d[rollno]=l1
        l.append(d)
        pickle.dump(d,f)
        print("Book is been Issued")
def k():
    return l