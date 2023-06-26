from DB.maindb import maindb

class viewBalance():

    def viewBalance():
        accountNumber = int(input("Please Enter your Account Number: "))

        maindb.getBalance(accountNumber)