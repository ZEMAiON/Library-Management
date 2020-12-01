from datetime import date
import time,pickle,LIBRARY_MANAGEMENT_PROJECT.ADMIN_PRIVILEGES.issueBook as k1
l1=[]
def returnBook(n1,rollno):
    l1=k1.k()
    if not l1:
        print("You dont have any book with this Name")
    else:
        sec1=time.time()
        ind=d1=sec2=0
        print(l1)
        for i in range(len(l1)):
            for j in l1[i]:
                if j==n1:
                    sec2=sec1-int(l1[i][j][1])
                    ind=l1.index(i)
        d1=str(date.fromtimestamp(sec2))
        print(d1)
        d2=d1.split("-")
        if(d2[1]=='01'):
            if int(d2[2])<10:
                with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/IssueBooks.pkl","wb") as f:
                    l1.pop(ind)
                    for i in range(len(l1)):
                        pickle.dump(l1[i],f)
                        l1.pop(ind)
                    print("Book is Being Back to Library")
            elif (int(d2[1][1])>1):
                print(f"Your Fine is {(d2[2]*int(d2[1][1])*30-10)*5}")
            else:
                print(f"Your Fine is {(d2[2]-10)*5}")

