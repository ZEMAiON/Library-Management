import pickle
def viewSPersonalDetails(rollno):
    with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/personaldet.dat",'rb') as f:
         while True:
            l=[]
            try:
                obj=pickle.load(f)
                for i in obj:
                    if rollno==i:
                        l=obj.get(i)
                        print(f"Rollno:{rollno}\nName:{l[0]}\nD.O.B.:{l[1]}\nBranch:{l[2]}\nYear Of Admission:{l[3]}")
            except Exception:
                break
     
    
    