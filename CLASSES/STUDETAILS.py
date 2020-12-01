import pickle
l=[]
class StuDetails:
    def __init__(s,rollno,name,dob,branch,yearofad):
        s.rollno=rollno
        s.name=name
        s.dob=dob
        s.branch=branch
        s.yearofad=yearofad    
        d={}
        l=[]
        l.append(s.name)
        l.append(s.dob)
        l.append(s.branch)
        l.append(s.yearofad)
        d[s.rollno]=l
        with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/personaldet.dat","ab") as f:
            pickle.dump(d,f)
        print()
        print("Student Details Added Successfully")
    