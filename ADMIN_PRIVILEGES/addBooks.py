import LIBRARY_MANAGEMENT_PROJECT.CLASSES.Books as b
def addBooks():
    n1,n2,n3=input("Enter Book name:"),input("Enter isbn no:"),input("Enter author name:")
    b1=b.Books(n1,n2,n3)