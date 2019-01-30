#library management system
from datetime import datetime
def home():
    a=1
    while a:
        print(" LIBRARY MANAGEMENT SYSTEM ".center(78,'$'))
        a=int(input('''Select a choice :
1.Admin login
2.Student login
3.Admin Signup
4.Student signup
0.Exit\n'''))
        if a is 1:
            adminlog()
        elif a is 2:
            stdlogin()
        elif a is 3:
            adminsign()
        elif a is 4:
            stdsign()
        elif a is 0:
            print("thanku for using library management system")
            exit()
        else:
            print("enter a valid choice")


def adminlog():
        a=1
        print("ADMIN LOGIN".center(78,'*'))
        b="%s,%s\n"%(input("enter the admin username\n"),input("enter the admin password\n"))
        if b in open("e:/cetpaproject/library management/admin.txt").read():
            print("      LOGGED IN    ".center(78,'@'))
            while a:
                print(" MENU ".center(79,'$'))
                a=int(input('''select a choice:
1.Add book
2.calculate fine
3.issue book
4.show books
0.Exit\n'''))
                if a is 1:
                    addbook()
                elif a is 2:
                    fine()
                elif a is 3:
                    issuebook()
                elif a is 4:
                    bookdetails()
                elif a is 0:
                    print("thanku for using admin login system")
                else:
                    print("enter a valid choice")

        
        else:
            print("invalid credentials")
        


 
def stdlogin():
    a=1
    
    print(" STUDENT LOGIN IN ".center(78,'*'))
    b="%s,%s,%s\n"%(input("enter the username\n"),input("enter the  password\n"),input("enter the roll number\n"))
    if b in open("e:/cetpaproject/library management/student.txt").read():
        print("  STUDENT LOGGEDIN  ")
        while a:
            a=int(input('''Select a choice:
                        1.showbooks
                        2.fine details
                        o.exit
                        '''))
            if a is 1:
                bookdetails()
            elif a is 2:
                fine()
            elif a is 0:
                print("thanku for using student portal")
            else:
                print("invalid credentials")
            
                
                    
                        
            
    else:
        print("invalid credentials")









def adminsign():
    print("ADMIN SIGNIN".center(78,'*'))
    b="%s,%s\n"%(input("enter the new admin username\n"),input("enter the new admin password\n"))
    if b.split(",")[0] in open("e:/cetpaproject/library management/admin.txt").read():
        print("user allready exists")
        adminsign()
    else:
        open("e:/cetpaproject/library management/admin.txt","a").write(b)
        adminlog()

        
def stdsign():
    print("STUDENT SIGIN".center(78,'*'))
    b="%s,%s,%s\n"%(input("enter the student name"),input("enter the password\n"),input("enter the roll number\n"))
    if b.split(",")[0] in open("e:/cetpaproject/library management/student.txt").read():
        print("user allready exists")
        stdsign()
    else:
        open("e:/cetpaproject/library management/student.txt","a").write(b)
        stdlogin()

def bookdetails():
    a=open("e:/cetpaproject/library management/books.txt").readlines()
    for i in range(len(a)):
        w=a[i].partition(",")
        print(w[0],"")



def addbook():
    print(" Enter the New Book ".center(78,"X"))
    b="%s,%s,%s,%s\n"%(input("enter the book name\n"),input("enter the isbn number\n"),input("enter the author name\n"),input("enter the status of the book:0-not issued 1-issued\n"))
    if b.split(",")[1] in open("e:/cetpaproject/library management/books.txt").read():
             print("book already present")
    if b.split(",")[3]=='1':
        open("e:/cetpaproject/library management/recordofissue.txt","a").write(b)
             
    else:
             open("e:/cetpaproject/library management/books.txt","a").write(b)
             print("Book Added")



def issuebook():
       bk=input(" enter the name of the book to be issued \n ") 
       a=open("e:/cetpaproject/library management/books.txt")
       e=a.readlines()
       for i in range(len(e)):
               d=e[i].partition(",")
               l=e[i].rpartition(",")
               if d[0]==bk:
                       if (l[2])=='0\n':
                                 f="%s,%s,%s,%s \n"%(d[0],input("enter roll number of student\n"),input("enter date of issue in format yyyy/mm/dd\n"),input("enter date of return in format yyyy/mm/dd\n"))
                                 open("e:/cetpaproject/library management/recordofissue.txt","a").write(f)
                                 print("book issued")
                       else:
                                 print("book already issued to someone")
            




def fine():
        bk=input(" enter the name of book for which the fine is to be seen ")
        a=open("e:/cetpaproject/library management/recordofissue.txt")
        e=a.readlines()
        for i in range (len(e)):
                d=e[i].partition(",")
                if d[0]==bk:
                        m=e[i].rpartition(",")
                        s=m[2].split("/")
                        p=int(s[0])
                        q=int(s[1])
                        r=int(s[2])
                        rdate=datetime(p,q,r) 
                        present_date=datetime.today()
                        dayss=(present_date-rdate).days
                        if dayss>0:
                              fine=5*dayss
                        else:
                             fine=0
                        print("your fine is",fine)
                              

       
                        
        
                                  
    
    
    
