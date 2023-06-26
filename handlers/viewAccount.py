from DB.maindb import maindb

class viewAccount():

    def viewData():

        accountNumber = int(input("Please Enter Account Number: "))
        cnic = int(input("Please Enter CNIC : "))

        maindb.getInfo(accountNumber, cnic)