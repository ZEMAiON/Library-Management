import pickle
l=[]
class FacDetails:
    def __init__(s,eid,name,dob,dep,yearofjoining):
        s.eid=eid
        s.name=name
        s.dob=dob
        s.dep=dep
        s.yearofjoining=yearofjoining
        d={}
        l.append(s.name)
        l.append(s.dob)
        l.append(s.dep)
        l.append(s.yearofjoining)
        d[s.eid]=l
        with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/personaldet.dat","ab") as f:
            pickle.dump(d,f)
        print()
        print("Faculty Details Added Successfully")