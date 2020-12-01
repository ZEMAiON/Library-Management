import LIBRARY_MANAGEMENT_PROJECT.PASSWORDS.pd as p1
import pickle,getpass
def changePassword(rollno):
    catchpreuser=p1.preExistingUser()
    p=getpass.getpass("new password:")
    with open("LIBRARY_MANAGEMENT_PROJECT/PROJECT_TEXT_FILES/pwd.dat",'wb') as f:
        for i in range(len(catchpreuser)):
            for j in catchpreuser[i]:
                if j==rollno:
                    catchpreuser[i][j][0]=p
        for i in range(len(catchpreuser)):
            pickle.dump(catchpreuser[i],f)
    print("Password Updated Successfully")    