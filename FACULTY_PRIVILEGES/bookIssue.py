import LIBRARY_MANAGEMENT_PROJECT.ADMIN_PRIVILEGES.issueBook as k,pickle
l1=[]
def bookIssue(eid):
    with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/Books.pkl","rb") as f:
        while True:
            try:
                obj=pickle.load(f)
                l1.append(obj)
            except Exception:
                break
    print("Book Available in Library are :")
    for i in range(len(l1)):
        for j in l1[i]:
            print(j)
    n=input("Book You Want To Issue:")
    k.issueBook(n,eid)
