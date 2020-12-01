import pickle 
import LIBRARY_MANAGEMENT_PROJECT.PASSWORDS.pd as p1
import LIBRARY_MANAGEMENT_PROJECT.CLASSES.FACDETAILS as f1
def new_faculty(u,p):
    catchpreuser=p1.preExistingUser()
    print()
    n1,n2,n3,n4=input("Name:"),input("D.O.B:"),input("Department:"),input("Year Of Joining:")
    Fac1=f1.FacDetails(u,n1,n2,n3,n4)
    with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/pwd.dat","ab") as f:
        d={}
        l=[]
        l.append(p)
        l.append('f')
        d[u]=l
        catchpreuser.append(d)
        pickle.dump(d,f)
    print("Faculty Added Successfully")
                
        