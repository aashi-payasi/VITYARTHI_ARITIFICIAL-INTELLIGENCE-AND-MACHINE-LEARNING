#withdraw_money.py
from account import account
from fraud_detector import is_suspicious, log_alert

def withdraw_amount():
    print("""
    ---------------------------
      Money Withdrawal System
    ---------------------------
    """)
    try:
        amount = float(input("Enter the withdrawal amount: ₹"))
    except ValueError:
        print("Invalid input. Please enter a numeric amount.")
        return
    if amount <= 0:
        print("Invalid amount. Withdrawal amount should be greater than 0. ")
        return

    balance = float(account.get('balance', 0.0))
    if amount > balance:
        print(f"Insufficient balance! Your current account balance is : ₹{balance:.2f}")
        return

    if is_suspicious(amount, balance):
        print("⚠ This withdrawal looks unusual for this account.")
        log_alert("withdraw", amount)
        confirm = input("Do you want to continue anyway? (y/n): ").strip().lower()
        if confirm != "y":
            print("Transaction cancelled.\n")
            return

    account['balance'] = balance - amount
    print(f"₹{amount:.2f} has been withdrawn from your account.")
    print(f"New balance: ₹{account['balance']:.2f}")
    print("Please collect your cash and receipt.\n")

if __name__ == "__main__":
    withdraw_amount()

