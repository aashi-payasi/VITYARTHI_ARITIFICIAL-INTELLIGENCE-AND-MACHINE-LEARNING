#withdraw_amount.py 

from account import account 

def withdraw_amount():
    print("""
---------------------------
 Money Withdrawal System
---------------------------
""")
    
    try:
        amount = float(input("Enter the withdrawal amount: \u20B9"))
    except ValueError:
        print("Invalid input. Please enter a numeric amount.")
        return
    
    if amount <= 0:
        print("Invalid amount. Withdrawal amount should be greater than 0. ")
        return
    
    balance = float(account.get('balance', 0.0))
    if amount > balance:
        print(f"Insufficient balance! Your current account balance is : \u20B9{balance:.2f}")
        return
    
    account['balance'] = balance - amount 
    print(f"\u20B9{amount:.2f} has been withdrawn from your account.")
    print(f"New balance: \u20B9{account['balance']:.2f}")
    print("Please collect your cash and recepit.\n")

if __name__ == "__main__":
   withdraw_amount()    
