import pickle
def viewFPersonalDetails(eid):
    with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/personaldet.dat",'rb') as f:
         while True:
            l=[]
            try:
                obj=pickle.load(f)
                for i in obj:
                    if eid==i:
                        l=obj.get(i)
                        print()
                        print(f"eid:{eid}\nName:{l[0]}D.O.B.:{l[1]}\nDep:{l[2]}\nYear Of Joining:{l[3]}")
            except EOFError:
                break