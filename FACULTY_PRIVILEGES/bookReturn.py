import LIBRARY_MANAGEMENT_PROJECT.ADMIN_PRIVILEGES.returnBook as k
def bookReturn(eid):
    n=input("Book You Want To Return:")
    k.returnBook(n,eid)