from DB.maindb import maindb
import datetime as date

class addAccount():

    def registerAccount():
        #getting all data from User
        name = input("Please Enter Your Name: ")
        cnic = input("Please Enter Your CNIC: ")
        fatherName = input("Please Enter Your Father Name: ")
        initialBalance = input("Please Enter Your Initial Balance: ")
        Date = date.date.today()

        #adding all data to file in maindb.py
        #returns account number
        accountNumber = maindb.addInfo(name, cnic, fatherName, initialBalance, Date)

        #print account Number
        print("Account at Bank of NUML Opened!!! Your Account Number is " + str(accountNumber))

 