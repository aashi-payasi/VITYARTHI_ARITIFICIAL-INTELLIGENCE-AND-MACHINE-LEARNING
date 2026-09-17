#deposit_money.py 

from account import account 


def deposit_amount():
    print("""
----------------------
 Money Deposit System
----------------------
 """)
    
    print("Welcome to ATM")

    try:
        amount = float(input("Please enter the amount to be deposited: \u20B9"))
    except ValueError:
        print("Invalid input. Please enter a numeric value")
        return
    
    if amount <= 0:
        print("Invalid Amount! Deposit amount should  be greater than 0.")
        return
    
    #Updating in-memory account balance:
    account['balance']= float(account.get('balance' , 0.0)) + amount 

    print(f"\u20B9{amount:2f} has been successfully deposited to your account")
    print(f"New balance:\u20B9{account['balance']:.2f}")
    print("Please collect your receipt.\n")
    print("Thankyou for using our ATM service!")

    if __name__ == "_main_":
       deposit_amount()


