import mysql.connector
sqlcon=mysql.connector.connect(host='localhost',user='root',passwd='root123',database='office_administration')
cursor=sqlcon.cursor()
cursor.execute("Create table IF NOT EXISTS Stock(Sno int(5) Primary key,IName varchar(20) Not Null,Date char(10),Qnty int(5) Not Null,cost int(6) Not Null)")
cursor.execute("Create table IF NOT EXISTS Sales(Slno int(5) Primary key,Iname varchar(20),Nameofemployee varchar(30) Not Null,Date char(10),Buyer varchar (20) Not Null,Qnty int(5) Not Null,Selling_Price int(7) Not Null)")
cursor.execute("Create table IF NOT EXISTS Revenue(Year int(4),Income int(8),Expense int(8),Total int(8))")
#employee module
def employeeadd(sqlcon,cursor):
    '''Adding a record to employee table'''
    n=int(input("Number of records to be added: "))
    for i in range (n):
        Eno=int(input("Employee no:"))
        Name=input("Employee name:")
        Age=int(input("Age:"))
        Dept=input("Department:")
        D_join=input("Date of join(dd-mm-yyyy):")
        Gender=input("Gender:")
        cursor.execute("insert into Employee values({},'{}',{},'{}','{}','{}')".format(Eno,Name,Age,Dept,D_join,Gender))
        sqlcon.commit()

def employeeupdate(sqlcon,cursor):
    '''Updating a record of employee table'''
    Eno=int(input("Enter Employee no to update details: "))
    print("New Details :")
    Name=input("Employee Name: ")
    Age=int(input("Age:"))
    Dept=input("Department:")
    D_join=input("Date of join(dd-mm-yyyy):")
    Gender=input("Gender:")
    cursor.execute("Update Employee set Name='{}',Age={},Dept='{}',D_join='{}',Gender='{}' Where Eno={}".format(Name,Age,Dept,D_join,Gender,Eno))
    sqlcon.commit()

def employeeview(cursor):
    '''Viewing all records of employee table'''

    cursor.execute("Select * from Employee ")
    records=cursor.fetchall()
    row=cursor.rowcount
    print("Records:\n",records,'\nTotal number of Employees=',row)

def employeedel(sqlcon,cursor):
    '''Deleting a record from employee '''
    Eno=int(input("Enter Employee no to be deleted: "))
    cursor.execute("Delete From Employee Where Eno={}".format(Eno))
    sqlcon.commit()

def employee(sqlcon,cursor):
    while True:
        print('''Options for table Employee :\n1.Enter the details of new employee.\n2.Update the details of an existing employee.
3.Delete records of an old employee.\n4.View the details of all employees.\n5.Go back.''')
        a_ch2=int(input("Your choice: "))
        if a_ch2 == 1 :
            employeeadd(sqlcon,cursor)
        elif a_ch2 == 2 :
            employeeupdate(sqlcon,cursor)
        elif a_ch2 == 3 :
            employeedel(sqlcon,cursor)
        elif a_ch2 == 4 :
            employeeview(cursor)
        elif a_ch2 == 5 :
            break
        else:
            print("Invalid option. Choice must be in (1-5)")
        cont=input("Do you wish to continue(y/n): ")
        if cont in 'nN':
            break
#Functions of revenue table
from mysqlcon import *
from datetime import date
today=date.today()                          #can give yr and others as parameters
date=today.strftime("%d/%m")

if date=='10/01':
    cursor.execute("Select year from Revenue")
    years=cursor.fetchall()  #previous years
    tdstr=str(today)
    yr=int(tdstr[0:4])    #-1    
    if (yr,) not in years:  
        cursor.execute("Select SUM(total) From Stock Where year(date)={}".format(yr))
        Cost=cursor.fetchone()
        cost=int(Cost[0])
        cursor.execute("Select SUM(Salary) From Salary")
        Slry=cursor.fetchone()
        slry=int(Slry[0])
        cursor.execute("Select SUM(totl) From Sales where year(date)={}".format(yr))   
        Slpr=cursor.fetchone()
        slpr=int(Slpr[0])
        exp=cost+slry    
        total=slpr-exp
        cursor.execute("Insert into Revenue values({},{},{},{})".format(yr,slpr,exp,total))
        sqlcon.commit()


def revenueview(cursor):
    '''Viewing revenue details'''
    cursor.execute("Select * From Revenue")
    view=cursor.fetchall()
    print(view)##improve

def revenueviewone(cursor):
    '''view revenue of a particular year'''
    year=int(input("Enter year: "))
    cursor.execute("Select * From Revenue where year={}".format(year))
    view=cursor.fetchone()
    print("Revenue of year ",year,": \n",view)##improve give it in proper based on output
    

def revenue(sqlcon,cursor):

    while True:
        print('''Options for table Revenue :\n1.View Revenue of all years.\n2.View Revenue of a specific year\n3.Go back to main menu''')
        a_ch4=int(input("Your Choice: "))
        if a_ch4 == 1 :
            revenueview(cursor)
        elif a_ch4 == 2 :
            revenueviewone(cursor)
        elif a_ch4 == 3 :
            break
        else:
            print("Invalid option. Choice must be in (1,2)")
        cont=input("Continue interacting with revenue table? (y/n): ")
        if cont in 'nN':
            break         #breaks out of functions loop
#options with salary table
def salaryadd(sqlcon,cursor):
    '''Adding a record to salary table'''
    n=int(input("Number of records to be added: "))
    for i in range (n):
        Eno=int(input("Employee no:"))
        Sal=int(input("Salary:"))
        Ben=int(input("Benefits:"))
        Des=input("Designation:")
        cursor.execute("insert into Salary values({},{},{},'{}')".format(Eno,Sal,Ben,Des))
        sqlcon.commit()
def salaryupdate(sqlcon,cursor):
    '''Updating a record of salary table'''

    Eno=int(input("Enter Employee no of the salary to be updated: "))
    print("New Details :")
    Sal=int(input("Salary:"))
    Ben=int(input("Benefits:"))
    Des=input("Designation:")
    cursor.execute("Update Salary set Salary={},Benefits={},Designation='{}' Where Eno={}".format(Sal,Ben,Des,Eno))
    sqlcon.commit()

def salaryview(cursor):
    '''Viewing all records of salary table'''

    cursor.execute("Select * from Salary ")
    records=cursor.fetchall()
    row=cursor.rowcount
    print("Records:\n",records,'\nTotal number of records=',row)

def salarydel(sqlcon,cursor):
    '''Deleting a record from salary'''
    Eno=int(input("Enter Employee no to be deleted: "))
    cursor.execute("Delete From Salary Where Eno={}".format(Eno))
    sqlcon.commit()

def salary(sqlcon,cursor):
    while True:
        print('''Options for table Stock :\n1.Enter the Salary of a new employee.\n2.Update the salary of an existing employee.
3.Delete the salary details of an old employee.\n4.View salary of all employees.\n5.Go back.''')
        a_ch3=int(input("Your choice: "))
        if a_ch3 == 1 :
            salaryadd(sqlcon,cursor)
        elif a_ch3 == 2 :
            salaryupdate(sqlcon,cursor)
        elif a_ch3 == 3 :
            salarydel(sqlcon,cursor)
        elif a_ch3 == 4 :
            salaryview(cursor)
        elif a_ch3 == 5 :
            break
        else:
            print("Invalid option. Choice must be in (1-5)")
        cont=input("Do you wish to continue(y/n): ")
        if cont in 'nN':
            break
#Functions using sales table
#try except
from datetime import date 
def newsale(sqlcon,cursor):
    '''Making a new sale'''    '''add price to table'''
    cursor.execute("Select MAX(Slno) From Sales")
    slno=cursor.fetchone()
    if slno ==None:
        slno=100
    else:
        slno=slno[0]
        slno+=1
    icod=int(input("Item Code: "))
    inam=input("Item Name: ")
    enam=input("Name of employee: ")
    buyr=input("Buyer: ")
    qnty=int(input("Quantity: "))
    slpr=int(input("Price: "))
    totl=qnty*slpr
    dte=date.today()  #gives the days date in yyyy-mm-dd
    if inam=='':
        cursor.execute("Select Iname From Stock Where sno={} ".format(icod))
        nam=cursor.fetchone()
        inam=nam
        inam=inam[0]

    cursor.execute("Insert into Sales values({},{},'{}','{}','{}','{}',{},{},{})".format(slno,icod,inam,enam,dte,buyr,qnty,slpr,totl))
    sqlcon.commit()
    cursor.execute("Select Qnty From Stock Where sno={} ".format(icod))
    Qty=cursor.fetchone()
    qty=int(Qty[0])
    qty=qty-qnty
    cursor.execute("Update Stock Set Qnty={} where sno={}".format(qty,icod))
    sqlcon.commit()

def viewsale(cursor):
    '''view all sales made'''
    cursor.execute("Select * From Sales ")
    sale=cursor.fetchall()
    print(sale)##improve

def sales(sqlcon,cursor):
    while True:
        print('''Options for table Sales :\n1.Make a sale.\n2.View all sales made.\n3.Go back to main menu''')
        a_ch6=int(input("Your Choice: "))
        if a_ch6 == 1 :
            newsale(sqlcon,cursor)
        elif a_ch6 == 2 :
            viewsale(cursor)
        elif a_ch6 == 3 :
            break
        else:
            print("Invalid option. Choice must be in (1,2)")
        cont=input("Continue iteracting with sales table ? (y/n): ")
        if cont in 'nN':
            break         #breaks out of functions loop
#Functions using stock table

def stockadd(sqlcon,cursor):
    '''Adding a record to stock table'''
    n=int(input("Number of records to be added: "))
    for i in range (n):
        sno=int(input("Item Code: "))
        inam=input("Item Name: ")
        date=input("Enter the date (yyyy-mm-dd): ")
        qnty=int(input("Quantity"))
        cost=int(input("Cost "))
        total=cost*qnty
        cursor.execute("Insert into Stock values({},'{}','{}',{},{},{})".format(sno,inam,date,qnty,cost,total))
        sqlcon.commit()

def stockupdate(sqlcon,cursor):
    '''Updating a record of stock table'''

    sno=int(input("Enter Item code of the stock to be updated: "))
    print("New Details :")
    inam=input("Item Name: ")
    date=input("Enter the date (yyyy-mm-dd): ")
    qnty=int(input("Quantity"))
    cost=int(input("Cost "))
    total=qnty*cost
    cursor.execute("Update Stock set Iname='{}',Date='{}',Qnty='{}',Cost={},total={} Where Sno={}".format(inam,date,qnty,cost,total,sno))
    sqlcon.commit()

def stockview(cursor):
    '''Viewing all records of stock table'''

    cursor.execute("Select * from Stock ")
    records=cursor.fetchall()
    row=cursor.rowcount
    print("Records: \n",records,"\nNo of items =",row)

def stockdel(sqlcon,cursor):
    '''Deleting a record from stock'''
    sno=int(input("Enter Code of item to be deleted: "))
    cursor.execute("Delete From Stock Where Sno={}".format(sno))
    sqlcon.commit()

def stock(sqlcon,cursor):
    while True:
        print('''Options for table Stock :\n1.Enter the details of new item.\n2.Update the details of an existing item.
3.Delete an item.\n4.View all items.\n5.Go back.''')
        a_ch5=int(input("Your choice: "))
        if a_ch5 == 1 :
            stockadd(sqlcon,cursor)
        elif a_ch5 == 2 :
            stockupdate(sqlcon,cursor)
        elif a_ch5 == 3 :
            stockdel(sqlcon,cursor)
        elif a_ch5 == 4 :
            stockview(cursor)
        elif a_ch5 == 5 :
            break
        else:
            print("Invalid option. Choice must be in (1-5)")
        cont=input("Do you wish to continue(y/n): ")
        if cont in 'nN':
            break
#Main program
'''CH-->user,ch1-->passwd,a_chx--> choosing tables'''  '''improve all print statements'''
import mysql.connector
from Employee import *
from Salary import *
from Revenue import *
from Stock import *
from Sales import *
adminpsswd="admin@123"
userpsswd="user@123"

sqlcon = mysql.connector.connect(host='localhost',user='root',passwd='root123')
if sqlcon.is_connected():
    print("Connected to database successfully")
    cursor=sqlcon.cursor()
    cursor.execute("Create database IF NOT EXISTS Office_Administration")
    cursor.execute("Use Office_Administration")

    cursor.execute("Create table IF NOT EXISTS Employee(Eno int Primary key,Name varchar(30),Age int,Dept varchar(30),D_join varchar(20),Gender char(10))")
    cursor.execute("Create table IF NOT EXISTS Salary(Eno int Primary key,Salary int(10),Benefits int(6),Designation varchar(25))")
    cursor.execute("Create table IF NOT EXISTS Stock(Sno int Primary key,IName varchar(20) Not Null,Date char(10),Qnty int Not Null,cost int Not Null,Total int Not Null)")
    cursor.execute("Create table IF NOT EXISTS Sales(Slno int Primary key,Icode int Not Null,Iname varchar(20),Nameofemployee varchar(30) Not Null,Date char(10),Buyer varchar (20) Not Null,Qty int Not Null,Selling_Price int Not Null,Totl int Not Null)")
    cursor.execute("Create table IF NOT EXISTS Revenue(Year int,Income int,Expense int,Total int)")
    def ownsalary(cursor):
        while True:
            print("\nView your salary")
            id=int(input("Enter your id : "))
            cursor.execute("Select * from Salary where eno={}".format(id))
            view=cursor.fetchone()
            print(view)
            cont=input("Press any key to go back ")
            break
    def stockviewone(cursor):
        while True:
            print("\nDisplaying all items in stock")
            stockview(cursor)
            cont=input("Press any key to go back ")
            break
    def owndet(cursor):
        while True:
            print("\nView own details ")
            id=int(input("Enter your id : "))
            cursor.execute("Select * from employee where Eno={}".format(id))
            view=cursor.fetchone()
            print(view)
            cont=input("Press any key to go back ")
            break
    #
    while True:
        print("\nLogin as :\n1.Admin \n2.Employee\n3.Exit")
        CH=input("Your Choice: ")  #main loop     #loop complete but have 2 fill user 

        if CH=='1':
            while True:                                                                                #admin loop
                ch1=input("\nEnter Admin password: ")
                if adminpsswd ==ch1:
                    while True:                                                                    #options loop      #loop complete but have to fill in options
                        print("\nAdmin Menu:\n1.Display all options\n2.Personal Details\n3.Salary\n4.Revenue\n5.Stock\n6.Sales\n7.Log out as Admin")
                        a_ch=input("Your choice: ")
                        if a_ch == '1' :
                            #total =16 p-4(ad,up,del,view),s-4(ad,up,del,view);rev-2(view,viewyr),stock-4,sale-2
                            opt='''All available Options :-\n1.Enter the details of new employee.\t\t2.Update the details of an existing employee.
3.Delete records of an old employee.\t\t4.View the details of all employees
5.Enter the Salary of a new employee.\t\t6.Update the salary of an existing employee.
7.Delete the salary details of an old employee.\t8.View salary of all employees.
9.View Revenue of all years.\t\t\t10.View Revenue of a specific year
11.Enter the details of new item in stock.\t\t12.Update the details of an existing item in stock.
13.Delete an item in stock.\t\t\t14.View all items in stock.
15.Make a sale.\t\t\t\t16.View all sales made.\n17.Go back'''
                            print(opt)
                            while True:
                                a_ch1=input("Your choice: ")
                                if a_ch1 == '1' :
                                    employeeadd(sqlcon,cursor)
                                elif a_ch1 == '2' :
                                    employeeupdate(sqlcon,cursor)
                                elif a_ch1 == '3' :
                                    employeedel(sqlcon,cursor)
                                elif a_ch1 == '4' :
                                    employeeview(cursor)
                                elif a_ch1 == '5' :
                                    salaryadd(sqlcon,cursor)
                                elif a_ch1 == '6' :
                                    salaryupdate(sqlcon,cursor)
                                elif a_ch1 == '7' :
                                    salarydel(sqlcon,cursor)
                                elif a_ch1 == '8' :
                                    salaryview(cursor)
                                elif a_ch1 == '9' :
                                    revenueview(cursor)
                                elif a_ch1 == '10' :
                                    revenueviewone(cursor)
                                elif a_ch1 == '11' :
                                    stockadd(sqlcon,cursor)
                                elif a_ch1 == '12' :
                                    stockupdate(sqlcon,cursor)
                                elif a_ch1 == '13' :
                                    stockdel(sqlcon,cursor)
                                elif a_ch1 == '14' :
                                    stockview(cursor)
                                elif a_ch1 == '15' :
                                    newsale(sqlcon,cursor)
                                elif a_ch1 == '16' :
                                    viewsale(cursor)
                                elif a_ch1 == '17' :
                                    break
                                else:
                                    print('Invalid choice\nChoice must be between(1-17)')
                                cont=input("\nGo back to all options -y,\ngo back to admin menu-n(y/n): ")
                                if cont in 'nN':
                                    break
                                else:
                                    opta_=input("Do you want to see all the options again(y/n): ")
                                    if opta_ in 'yY':
                                        print(opt)

                        elif a_ch == '2' :
                            employee(sqlcon,cursor)
                        elif a_ch == '3':
                            salary(sqlcon,cursor)
                        elif a_ch == '4' :
                            revenue(sqlcon,cursor)                                                             #function loop
                        elif a_ch == '5' :
                            stock(sqlcon,cursor)
                        elif a_ch == '6' :
                            sales(sqlcon,cursor)
                        elif a_ch == '7' :
                            k=1
                            break   # breaks out of options loop
                        else:
                            print("\nInvalid choice.Choice must be within 1-6")
                            inp=input("Press any key to continue")
                    if k==1 :
                        break #breaks out of admin loop
                else:
                    print("Wrong Password")

        elif CH=='2':
            while True:
                ch2=input("\nEnter User password: ")
                if userpsswd ==ch2:
                    while True:                                                                    #options loop      #loop complete but have to fill in options
                        print("\nEmployee Menu :\n1.Display all options\n2.Personal Details\n3.Salary\n4.Revenue\n5.Stock\n6.Sales\n7.Log out as User")
                        u_ch=input("Option: ")
                        if u_ch == '1' :
                            opt='''All available options:\n1.Display own details.\t\t2.Display own salary.
3.Revenue of previous years.\t4.Revenue of a particular year
5.View Stock details.\t\t6.Make a sale
7.View all sales.\t\t8.Go back'''
                            print(opt)
                            while True:
                                u_ch1=input("Your choice: ")
                                if u_ch1 == '1' :
                                    owndet(cursor)
                                elif u_ch1 == '2' :
                                    ownsalary(cursor)
                                elif u_ch1 == '3' :
                                    revenueview(cursor)
                                elif u_ch1 == '4' :
                                    revenueviewone(cursor)
                                elif u_ch1 == '5' :
                                    stockviewone(cursor)
                                elif u_ch1 == '6' :
                                    newsale(sqlcon,cursor)
                                elif u_ch1 == '7' :
                                    viewsale(cursor)
                                elif u_ch1 == '8' :
                                    break
                                else:
                                    print('Invalid choice\nChoice must be between(1-8)')
                                cont=input("Do you wish to continue(y/n): ")
                                if cont in 'nN':
                                    break
                                else:
                                    opta_=input("Do you want to see the options again(y/n): ")
                                    if opta_ in 'yY':
                                        print(opt)
                        #personal
                        elif u_ch == '2' :
                            owndet(cursor)
                        elif u_ch == '3' :
                            ownsalary(cursor)
                        elif u_ch == '4' :                 #while True
                            revenue(sqlcon,cursor) 
                        elif u_ch == '5' :
                            stockviewone(cursor)
                        elif u_ch == '6' :
                            sales(sqlcon,cursor)
                        elif u_ch == '7' :
                            k=1
                            break   # breaks out of options loop
                        else:
                            print("Invalid choice.Choice must be within 1-6")
                            inp=input("Press any key to continue")
                    if k==1 :
                        break #breaks out of user loop
                else:
                    print("Wrong Password")

        elif CH=='3':
            sqlcon.close()
            print("Connection terminated\nClosing Program....")
            exit()
        else:
            print('wrong choice')  
