#deposit_money.py
from account import account
from fraud_detector import is_suspicious, log_alert

def deposit_amount():
    print("""
    ----------------------
      Money Deposit System
    ----------------------
    """)
    print("Welcome to ATM")
    try:
        amount = float(input("Please enter the amount to be deposited: ₹"))
    except ValueError:
        print("Invalid input. Please enter a numeric value")
        return
    if amount <= 0:
        print("Invalid Amount! Deposit amount should be greater than 0.")
        return

    balance_before = float(account.get('balance', 0.0))

    if is_suspicious(amount, balance_before):
        print("⚠ This deposit looks unusual for this account. It has been flagged for review.")
        log_alert("deposit", amount)

    account['balance'] = balance_before + amount
    print(f"₹{amount:.2f} has been successfully deposited to your account")
    print(f"New balance:₹{account['balance']:.2f}")
    print("Please collect your receipt.\n")
    print("Thankyou for using our ATM service!")

if __name__ == "__main__":
    deposit_amount()

