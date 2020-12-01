import pickle
def searchBook():
    c=0
    n1=input("Enter Book name to be searched:")
    with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/Books.pkl","rb") as f:
        while True:
            try:
                obj=pickle.load(f)
                for i in obj:
                    if n1.upper()==i.upper():
                        print(f"{n1} is available")
                        c+=1
            except EOFError:
                if c!=1:
                    print(f"{n1} isn't available")
                break
    
    