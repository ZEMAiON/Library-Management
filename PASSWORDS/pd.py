import pickle
import getpass
l,l1,l2=[],[],[]
def existUser():
    with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/pwd.dat","rb") as f:
        while True:
            try:
                obj=pickle.load(f)
                l1.append(obj)
            except Exception:
                break
    if len(l1)==0:
        with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/pwd.dat","wb") as f:
            d={"0187cs171121":["itesh","a"]}
            d1={"0187cs171175":["ash","s"]}
            d2={"0187csemp01":["ahul","f"]}
            d3={"0187cs171125":["ohit","s"]}
            l.append(d)
            l.append(d1)
            l.append(d2)
            l.append(d3)    
            pickle.dump(d,f)    
            pickle.dump(d1,f)
            pickle.dump(d2,f)
            pickle.dump(d3,f)
def preExistingUser():
    return l
def personalDet():
    with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/personaldet.dat",'rb') as f:
        while True:
            try:
                obj=pickle.load(f)
                l2.append(obj)
            except Exception:
                break
        if len(l2)==0:
            with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/personaldet.dat",'wb') as f:
                d1={"0187cs171121":["ritesh","31/10/99","cse","2017"]},
                d2={"0187cs171175":["ash","6/4/99","cse","2017"]}
                d3={"0187csemp01":["ahul","19/8/83","cse","2012"]}
                d4={"0187cs171125":["ohit","7/9/99","cse","2017"]}
                pickle.dump(d1,f)
                pickle.dump(d2,f)
                pickle.dump(d3,f)
                pickle.dump(d4,f)
def getobj1():
    l=[]
    with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/pwd.dat","rb") as f:
        while True:
            try:
                obj=pickle.load(f)
                l.append(obj)
            except Exception:
                return l
                break

def checkPass(ob):
    a=''
    c=0
    usern=input("Username:")
    password=getpass.getpass("Password:")
    for i in range(len(ob)):
        for j in ob[i]:
            if j==usern:
                if ob[i][j][0]==password:
                    a=ob[i][j][1]
                    print(f"Welcome To library:{usern}")
                    c=1
                    break
    if c==0:
        print("Wrong Username or Password")
    return usern,a
 
        
       
            
    