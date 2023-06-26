import random as rand
import csv

class maindb(): 

    def addInfo(name, cnic, fatherName, initialBalance, Date): 
        accountNumber = rand.randint(1, 10000000)
        file = open('File/accountDetails.csv', "a")
        dataOfBenificary = str(accountNumber) + "," + str(name) + "," + str(cnic) + "," + str(fatherName) + "," + str(initialBalance) + "," + str(Date) + "\n"
        file.write(dataOfBenificary)
        file.close()

        return accountNumber
    
    def getInfo(accountNumber, cnic):

        # Open the CSV file
        with open('File/accountDetails.csv', 'r') as file:
            # Create a CSV reader object
             reader = csv.reader(file)

        # Iterate over each row in the CSV file
             for row in reader:
                # Access each value in the current row
                if str(accountNumber) == str(row[0]) :
                    if str(cnic) == str(row[2]) :
                        print("| Account Number is " + str(row[0]) + "|")
                        print("| Name  is " + str(row[1]) + "|")
                        print("| Father Name  is " + str(row[3]) + "|")
                        print("| CNIC is " + str(row[2]) + "|")
                        print("| Balance  is " + str(row[4]) + "|")
                        print("| Date of Opening  is " + str(row[5]) + "|")
                        status = 1
                        break
                
                if status == 0:
                    print("No Records Found") 

    def getBalance(accountNumber):

        with open('File/accountDetails.csv', 'r') as file:

            reader = csv.reader(file)

            for row in reader:
                if str(accountNumber) == str(row[0]):
                    print("Your Account Balance is " + str(row[4]) + " Mr. " + str(row[1]))
                else:
                    print("Wrong Account Number")

            
        


        
        