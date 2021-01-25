import bankAccount_class

def main():

    print("Hello")

    start_bal = float(input("Enter the starting balance: "))

    owner = input("Enter your name: ")

    savings = bankAccount_class.BankAccount(start_bal, owner)

    print(savings)
    #print("Balance is: ",
          #format(savings.get_balance(), ',.2f'), sep='')

    amount = float(input("Enter the amount to be deposited: "))
    savings.deposit(amount)
    
    print(savings)
    #print("Balance is: ",
          #format(savings.get_balance(), ',.2f'), sep='')

    amount = float(input("Enter the amount to be withdrawn: "))
    savings.withdraw(amount)

    print(savings)
    #print("Balance is: ",
         # format(savings.get_balance(), ',.2f'), sep='')
    
main()
    
