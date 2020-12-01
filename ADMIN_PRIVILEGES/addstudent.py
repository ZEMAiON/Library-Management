import pickle
import LIBRARY_MANAGEMENT_PROJECT.PASSWORDS.pd as p1
import LIBRARY_MANAGEMENT_PROJECT.CLASSES.STUDETAILS as s
def new_student(u,p):
    catchpreuser=p1.preExistingUser()
    print()
    n1,n2,n3,n4=input("Name:"),input("D.O.B:"),input("Branch:"),input("Year Of Admission:")
    Stud=s.StuDetails(u,n1,n2,n3,n4)
    with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/pwd.dat","ab") as f:
        d={}
        l=[]
        l.append(p)
        l.append('s')
        d[u]=l
        catchpreuser.append(d)
        pickle.dump(d,f)
    print("Student Added Successfully")