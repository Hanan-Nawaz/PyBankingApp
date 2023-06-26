from handlers.addAccount import addAccount
from handlers.viewAccount import viewAccount

print("----------------------")
print("|    Bank of NUML    |")
print("----------------------")
print("| 1 |  Open Account  |")
print("----------------------")
print("| 2 | Deposite Money |")
print("----------------------")
print("| 3 | Withdraw Money |")
print("----------------------")
print("| 4 |  View Balance  |")
print("----------------------")
print("| 5 |  View History  |")
print("----------------------")
print("| 6 | Close  Account |")
print("----------------------")
print("| 7 | View   Account |")
print("----------------------")
print("| 8 |   Close  App   |")
print("----------------------")

choiceOfUser = int(input("Please Enter Choice: "))

match choiceOfUser:
    case 1 :
        addAccount.registerAccount()
    
    case 2 : 
        print(choiceOfUser)

    case 3 :
        print(choiceOfUser)
    
    case 4 : 
        print(choiceOfUser)
    
    case 5 :
        print(choiceOfUser)
    
    case 6 : 
        print(choiceOfUser)

    case 7 :
        viewAccount.viewData()

    case 8 :
        print(choiceOfUser)
    
    case _ : 
        print("Please Enter Valid Input")


