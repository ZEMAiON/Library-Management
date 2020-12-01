import sys,LIBRARY_MANAGEMENT_PROJECT.CLASSES.Books as pd2
import LIBRARY_MANAGEMENT_PROJECT.PASSWORDS.pd as pd1
import LIBRARY_MANAGEMENT_PROJECT.ADMIN_PRIVILEGES.searchBook as s1
import LIBRARY_MANAGEMENT_PROJECT.ADMIN_PRIVILEGES.addBooks as s2
import LIBRARY_MANAGEMENT_PROJECT.ADMIN_PRIVILEGES.addfaculty as s3
import LIBRARY_MANAGEMENT_PROJECT.ADMIN_PRIVILEGES.addstudent as s4
import LIBRARY_MANAGEMENT_PROJECT.ADMIN_PRIVILEGES.issueBook as s5
import LIBRARY_MANAGEMENT_PROJECT.ADMIN_PRIVILEGES.returnBook as s6
import LIBRARY_MANAGEMENT_PROJECT.ADMIN_PRIVILEGES.changePassword as s7
import LIBRARY_MANAGEMENT_PROJECT.STUDENT_PRIVILEGES.bookIssue as b1
import LIBRARY_MANAGEMENT_PROJECT.STUDENT_PRIVILEGES.bookReturn as b2
import LIBRARY_MANAGEMENT_PROJECT.STUDENT_PRIVILEGES.changePassword as b3
import LIBRARY_MANAGEMENT_PROJECT.STUDENT_PRIVILEGES.viewSPersonalDetails as b4
import LIBRARY_MANAGEMENT_PROJECT.FACULTY_PRIVILEGES.bookIssue as b5
import LIBRARY_MANAGEMENT_PROJECT.FACULTY_PRIVILEGES.bookReturn as b6
import LIBRARY_MANAGEMENT_PROJECT.FACULTY_PRIVILEGES.changePassword as b7
import LIBRARY_MANAGEMENT_PROJECT.FACULTY_PRIVILEGES.viewFPersonalDetails as b8
pd1.existUser()
pd1.personalDet()
pd2.LoadBooks()
def show():
    print("*"*40)
    print("WELCOME LIBRARY MANAGEMENT SYSTEM")
    print("*"*40)
    print() 
    ob=pd1.getobj1()
    re,a=pd1.checkPass(ob)
    if a=='s':
        while True:
            print()
            print("*"*20)
            print("1.Search Book")
            print("2.Issue Book")
            print("3.Return Book")
            print("4.Change Password")
            print("5.View Personal Details")
            print("6.logout")
            choice=int(input("Choice:"))
            if choice==1:
                s1.searchBook()
            elif choice==2:
                b1.bookIssue(re)
            elif choice==3:
                b2.bookReturn(re)
            elif choice==4:
                b3.changePassword(re)
            elif choice==5:
                b4.viewSPersonalDetails(re) 
            elif choice==6:
                sys.exit()
            else:
                print("Choose Carefully")
    if a=='f':
        while True:
            print()
            print("*"*20)
            print("1.Search Book")
            print("2.Issue Book")
            print("3.Return Book")
            print("4.Change Password")
            print("5.View Personal Details")
            print("6.Logout")
            choice=int(input("Choice:"))
            if choice==1:
                s1.searchBook()
            elif choice==2:
                b5.bookIssue(re)
            elif choice==3:
                b6.bookReturn(re)
            elif choice==4:
                b7.changePassword(re)
            elif choice==5:
                b8.viewFPersonalDetails(re) 
            elif choice==6:
                sys.exit()
            else:
                print("Choose Carefully")
    if a=='a':
        while True:
            print()
            print("*"*20)
            print("1.Add Book in Library")
            print("2.Add New Student Library DB")
            print("3.Add New Faculty Library DB")
            print("4.Search Book")
            print("5.Change Password")
            print("6.Logout")
            choice=int(input("Choice:"))
            if choice==1:
                s2.addBooks()
            elif choice==2:
                u,p=input("Rollno:"),input("Password:")
                s4.new_student(u,p)
            elif choice==3:
                u,p=input("Eid:"),input("Password:")
                s3.new_faculty(u,p)
            elif choice==4:
                s1.searchBook()
            elif choice==5:
                s7.changePassword(re) 
            elif choice==6:
                sys.exit()
            else:
                print("Choose Carefully")