import sys;
import MySQLdb;  
import re  
from _pyio import __metaclass__
from random import randint
import datetime 
con = MySQLdb.connect("localhost","root","","pydbm5" )
cur = con.cursor()
__metaclass__=type
class Customer:
    def __init__(self,AccountNo,CustomerName,AddressLine,City,Zip,State,PhoneNo,AdharNo,AccountType,Balance):
        self.__AccountNo = AccountNo
        self.__CustomerName = CustomerName
        self.__AddressLine =AddressLine
        self.__City = City
        self.__Zip = Zip
        self.__State = State
        self.__PhoneNo = PhoneNo
        self.__AdharNo = AdharNo
        self.__Balance = Balance
        self.__AccountType = AccountType
    def getAccountNo(self):
        return self.__AccountNo
    def getCustomerName(self):
        return self.__CustomerName


    def getAddressLine(self):
        return self.__AddressLine
    def getCity(self):
        return self.__City
    def getZip(self):
        return self.__Zip
    def getState(self):
        return self.__State
    def getPhoneNo(self):
        return self.__PhoneNo
    def getAdharNo(self):
        return self.__AdharNo
    def getBalance(self):
        return self.__Balance
    def getAccountType(self):
        return self.__AccountType
    def getUserName(self):
        return self.__UserName
    def setAccountNo(self, value):
        self.__AccountNo = value
    def setCustomerName(self, value):
        self.__CustomerName = value
    def setAddressLine(self, value):
        self.__AddressLine = value
    def setCity(self, value):
        self.__City = value
    def setZip(self, value):
        self.__Zip = value

    def setState(self, value):
        self.__State = value
    def setPhoneNo(self, value):
        self.__PhoneNo = value
    def setAdharNo(self, value):
        self.__AdharNo = value
    def setBalance(self, value):
        self.__Balance = value
    def setAccountType(self, value):
        self.__AccountType = value
    def validateZip(self):
        if len(self.__Zip) != 6 or str(self.__Zip).isdigit() == False:
            return False
        else:
            return True      
    def validatetelephoneno(self):
        if len(self.__telephoneno) != 10 or str(self.__telephoneno).isdigit() == False:
            return False
        else:
            return True
    def DisplayCustomerInformation(self):
        print "=============================================="
        print "Account Number  : " , self.__AccountNo
        print "Customer Name   : " , self.__CustomerName
        print "AddressLine     : " , self.__AddressLine
        print "City            : " , self.__City
        print "Zip             : " , self.__Zip
        print "State           : " , self.__State

        print "Phone Number    : " , self.__PhoneNo
        print "Adhar Number    : " , self.__AdharNo
        print "Balance         : " , self.__Balance
        if int(self.__AccountType)==0:
            print "AccountType     : Savings" 
        else:
            print "AccountType     :Current"
        print "=============================================\n"
class Main:
    Wish = 'n'
    LoginStatus = 0
    Admin=''
    Amount,AccountNo=int(0),0
    info=[]
    count=int(0)
    transtype=''
    UserName,Password="",""
    date=''
    transid=0
    status=''
    State=''
    Repay=''
    faccount=0 
    def LoginOptions(self):
        print("************************************")
        print("          Bank Application          ")
        print("************************************")


        print("        1. Login                    ")
        print("        2. Exit                     ")
        print("************************************")
        n = raw_input("Enter your choice    :  ")
        if n == '1':
            self.Login()
        elif n == '2':
            print("....!!! Thank You For Visiting !!!....")
            sys.exit
        else:
            print("=======================")
            print("Enter The Valid Choice")
            print("=======================\n")
            Main.LoginOptions(self)            
    def Options(self):
        if self.LoginStatus==1 and self.Admin=="Admin":
            print("************************************")
            print("          Bank Application          ")
            print("************************************")
            print("        1. Create New Account       ")
            print("        2. Deposite                 ")
            print("        3. Withdraw                 ")
            print("        4. Check Status             ")
            print("        5. Close Account            ")
            print("        6. Exit                     ")
            print("************************************")
            n = raw_input("Enter your choice    :  ")


            if n == '1':
                   self.CreateAccount()
            elif n == '2':
                    self.Deposite()
            elif n == '3':
                    self.Withdraw()
            elif n == '4':
                    self.AccountState()
            elif n == '5':
                    self.CloseAccount()
            elif n == '6':
                print("======================================")
                print("....!!! Thank You For Visiting !!!....")
                print("======================================\n")
                sys.exit
            else:
                print("======================")
                print("Enter The Valid Choice")
                print("======================\n")
                Main.Options(self)
        else:
            print("************************************")
            print("          Bank Application          ")
            print("************************************")
            print("        1. Apply Loan               ")
            print("        2. Fixed Deposite           ")
            print("        3. Check Balance            ")


            print("        4. Mini State               ")
            print("        5. View Account Information ")
            print("        6. Exit                     ")
            print("************************************")
            n = raw_input("Enter your choice    :  ")
            if n == '1':
                self.ApplyLoan()
            elif n == '2':
                self.FixedDeposite()
            elif n == '3':
                self.CheckBalance()
            elif n == '4':
                    self.MiniState()
            elif n == '5':
                    self.ViewAccountInformation()
            elif n == '6':
                print("======================================")
                print("....!!! Thank You For Visiting !!!....")
                print("======================================")
                sys.exit
            else:
                print("=======================")
                print ("Enter The Valid Choice")
                print("=======================\n")
                Main.Choice(self)         
   def Login(self):
        cusobj=Customer(None,None,None,None,None,None,None,None,None,None)
        self.UserName=raw_input("Enter User Name [Account Number]: ")

        self.Password=raw_input("Enter Password                  : ")
        cur.execute("select * from login where username = %s and password=%s",[self.UserName,self.Password])
        if cur.rowcount >0:
            if self.UserName =="Admin":
                    self.Admin="Admin"
                    self.LoginStatus=1
                    print("=====================")
                    print("Login Success")
                    print("=====================\n")
                    Main.Choice(self)
            else:
                cur.execute("select Status from customer where AccountNo= %s",[self.UserName])
                self.status=cur.fetchone()[0]
                self.state=self.status[0:len(self.status)-6]
                self.status=self.status[len(self.status)-6:]
                if self.status=="Opened":
                    print("=====================")
                    print("Login Success")
                    print("=====================\n")
                    Main.Choice(self)
                else:
                    print("======================================")
                    print "Account Is Closed Please Contact Admin"
                    print("======================================\n")
                    sys.exit
        else:
            print("=====================")	
            print("Enter Valid Details")

            print("=====================\n")
            Main.LoginOptions(self)        
    def ApplyLoan(self):
        cur.execute("select LoanAmount from loan where AccountNo= %s ",[self.UserName])
        if cur.rowcount >0:
            self.count=int( cur.fetchone()[0])
            print("==========================================")
            print "Your Already Have Loan Amount", self.count
            print("===========================================\n")
            Main.Choice(self)
        else:
            self.Amount=int(raw_input("Enter The Amount For Apply Loan  :"))
            self.Repay=raw_input("Enter The Repay Date [yyyy-mm-dd]:")
            cur.execute("select Balance from customer where AccountNo= %s",[self.UserName])
            self.count=int( cur.fetchone()[0])
            self.status=0
            cur.execute("select * from customer where AccountNo= %s and AccountType =%s ",[self.UserName,self.status])
            if cur.rowcount >0:
                if self.Amount < self.count :
                    self.state="NotPaid"
                    cur.execute("insert into loan values(%s,%s,%s,%s)",[self.UserName,self.Amount,self.Repay,self.state])
                    self.count=self.count+self.Amount
                    cur.execute("update Customer set Balance = %s where AccountNo = %s",[self.count,self.UserName])
                    con.commit()
                    print("=================================================")
                    print "Loan Granted Your current Balance is ",self.count
                    print("==================================================\n")


                    Main.Choice(self)
                else:
                    print("==================================")
                    print " Not Elegible Application Rejected"
                    print("==================================\n")
                    Main.Choice(self)
            else:
                print("==========================================")
                print "Insufficient Balance  Application Rejected"
                print("===========================================\n")
                Main.Choice(self)        
    def FixedDeposite(self):
        cur.execute("select * from fixeddeposite where AccountNo= %s ",[self.UserName])
        if cur.rowcount >0:
            print("=============================")
            print "You Already Have An Acount "
            print("=============================\n")
            Main.Choice(self)
        else:
            cur.execute("select AccountType from customer where AccountNo= %s ",[self.UserName])
            if cur.rowcount >0:
                self.count=int( cur.fetchone()[0])
                if self.count ==1:
                    print("==========================================")
                    print "Your Not Elegible For Fixed Deposite"
                    print("===========================================\n")
                    Main.Choice(self)
                else:

                    self.Amount=int(raw_input("Enter The Amount of Fixed Deposite  :"))
                    self.Repay=int(raw_input("Enter The Duration in months:"))
                    if self.Repay <=12 or self.Amount <1000:
                        print("================================================================================")
                        print "Enter Valid Details Minimum Amount Is Rs.1000 /- and Minimum Duration 12 Months "
                        print("==============================================================================\n")
                        Main.Choice(self)
                    else:
                        self.faccount=randint(10000000001,99999999999)
                        now = datetime.datetime.now()
                        self.date=now.strftime("%Y-%m-%d")
                        cur.execute("insert into fixeddeposite values(%s,%s,%s,%s,%s)",[self.UserName,self.Repay,str(self.Amount),self.faccount,self.date])
                        con.commit()
                        print("============================================================================")
                        print "Your Account Is Created Fixed Deposite Account Number" ,self.faccount
                        print("============================================================================\n")
                        Main.Choice(self)            
    def CreateAccount(self):
        curobj=Customer(None,None,None,None,None,None,None,None,None,None)
        print("*****************Account Information***************")
        curobj.setAccountNo(randint(1000000000000001,9999999999999999))
        curobj.setCustomerName(raw_input("Enter Your Name     :  "))
        curobj.setAccountType(raw_input("Enter Your Account Type \n 0.Saving Account \n 1.Current Account\n    :  "))
        curobj.setAddressLine(raw_input("Enter Your Address  :  "))
        curobj.setCity(raw_input("Enter Your City     : "))


        curobj.setZip(raw_input("Enter Your ZipCode  : "))
        curobj.setState(raw_input("Enter Your State    : "))
        curobj.setPhoneNo(raw_input("Enter Your PhoneNo  : "))
        curobj.setAdharNo(raw_input("Enter Your Adhar No : "))
        curobj.setBalance('0')
        now = datetime.datetime.now()
        self.status=now.strftime("%Y-%m-%d")+"Opened"
        print("****************************************************")
cur.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[curobj.getAccountNo(),curobj.getCustomerName(),curobj.getAddressLine(),curobj.getCity(),curobj.getZip(),curobj.getState(),curobj.getPhoneNo(),curobj.getAdharNo(),curobj.getBalance(),curobj.getAccountType(),self.status])
        cur.execute("insert into login values(%s,%s)",[curobj.getAccountNo(),curobj.getAccountNo()])
        con.commit()
        print("===============")
        print("Account Created")
        print("===============\n")
        print ""
        curobj.DisplayCustomerInformation()
        Main.Choice(self)
    def Deposite(self):
        self.AccountNo=raw_input("Enter the Account Number you Want To Deposite :  ")       
        self.Amount=raw_input("Enter the Amount Want to Deposite :  ")
        cur.execute("select * from Customer where AccountNo=%s",[self.AccountNo])
        if cur.rowcount >0:
            cur.execute("select Balance from customer where AccountNo= %s",[self.AccountNo])
            print("*****************************************")
            self.count=int( cur.fetchone()[0])
            self.Amount=int(self.Amount)+int(self.count)


            cur.execute("update Customer set Balance = %s where AccountNo = %s",[self.Amount,self.AccountNo])
            now = datetime.datetime.now()
            self.date=now.strftime("%Y-%m-%d")
            self.transid=now.strftime("%Y%m%d%H%M%S")
            self.transtype="Deposite"
            cur.execute("insert into transaction values(%s,%s,%s,%s,%s)",[self.AccountNo,self.transtype,self.transid,self.Amount,self.date])
            con.commit()
            print "Your Current Balance is" ,self.Amount
            print("===================")
            print("Transaction Success")
            print("===================\n")
            Main.Choice(self)
        else:
            print("==========================")
            print("Enter Valid Account Number")
            print("==========================\n")
            Main.Choice(self)
    def CloseAccount(self):
        self.AccountNo=raw_input("Enter The Account Number You Want Close :")
        now = datetime.datetime.now()
        self.status=now.strftime("%Y-%m-%d")+"Closed"
        cur.execute("update Customer set Status = %s where AccountNo = %s",[self.status,self.AccountNo])
        con.commit()
        print("==============")
        print("Account Closed")
        print("==============\n")
        Main.Choice(self)


       def Withdraw(self):
        self.AccountNo=raw_input("Enter the Account Number you Want To Deposite :  ")       
        self.Amount=int(raw_input("Enter the Amount Want to Withdraw :  "))
        cur.execute("select * from Customer where AccountNo=%s",[self.AccountNo])
        if cur.rowcount >0:
            cur.execute("select Balance from customer where AccountNo= %s",[self.AccountNo])
            print("*****************************************")
            self.count=int( cur.fetchone()[0])
            if self.Amount < self.count and self.count >500:
                self.Amount=int(self.count)-int(self.Amount)
                cur.execute("update Customer set Balance = %s where AccountNo = %s",[self.Amount,self.AccountNo])
                now = datetime.datetime.now()
                self.date=now.strftime("%Y-%m-%d")
                self.transid=now.strftime("%Y%m%d%H%M%S")
                self.transtype="Deposite"
                cur.execute("insert into transaction values(%s,%s,%s,%s,%s)",[self.AccountNo,self.transtype,self.transid,self.Amount,self.date])
                con.commit()
                print "Your Current Balance is" ,self.Amount
                print("===================")
                print("Transaction Success")
                print("===================\n")
                Main.Choice(self)
            else:
                print("=====================")
                print "Insufficient Balance "
                print("=====================\n")
                Main.Choice(self)


        else:
            print("==========================")
            print("Enter Valid Account Number")
            print("==========================\n")
            Main.Choice(self)
    def CheckBalance(self):
        cur.execute("select Balance from customer where AccountNo= %s",[self.UserName])
        print("========================================")
        print "Your Current Balance Is",cur.fetchone()[0]
        print("========================================\n")
        con.commit()
        Main.Choice(self)
    def MiniState(self):
        cur.execute("select * from transaction where AccountNo= %s order by TransactionID",[self.UserName])
        print("==================================================================")
        self.info=cur.fetchall()
        print "Account Number\t    TransType\tTransactionID\tBalance\t   Date"
        while(self.count<cur.rowcount):
            print self.info[self.count]
            self.count=self.count+1
        print("===================================================================n")
        con.commit()
        Main.Choice(self)
    def ViewAccountInformation(self):
        cur.execute("select * from customer where AccountNo= %s ",[self.UserName])
        print("=====================================================")
        self.info=cur.fetchone()
        print "Account Number  : " , self.info[0]

        print "Customer Name   : " , self.info[1]
        print "AddressLine     : " , self.info[2]
        print "City            : " , self.info[3]
        print "Zip             : " , self.info[4]
        print "State           : " , self.info[5]
        print "Phone Number    : " , self.info[6]
        print "Adhar Number    : " , self.info[7]
        print("======================================================\n")
        con.commit()
        Main.Choice(self)
    def AccountState(self):
        self.AccountNo=raw_input("Enter The Account Number You Want Check :")
        cur.execute("select Status from customer where AccountNo= %s",[self.AccountNo])
        self.status=cur.fetchone()[0]
        self.state=self.status[0:len(self.status)-6]
        self.status=self.status[len(self.status)-6:]
        if self.status=="Opened":
            print("==============================================================")
            print "Account Is Active Now Opened On ",self.state
            print("==============================================================\n")
        else:
            print("==================")
            print "Account Is Closed "
            print("==================\n")
        Main.Choice(self)
    def Choice(self):
        Wish=raw_input("Do you want to continue(y/n) : ")
        if Wish in ('y', 'Y'):
            Main.Options(self)
        else:
            sys.exit
obj = Main()
obj.LoginOptions()
