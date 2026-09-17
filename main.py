def main():
    while True:
        print("\n --- ATM SYSTEM MENU ---")
        print("1. Login")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Fraud Alerts")
        print("6. Exit")

        choice = input("Enter your choice (1-6):")

        if choice == '1':
            from login_page import login
            login()
        elif choice == '2':
            from deposit_money import deposit_amount
            deposit_amount()
        elif choice == '3':
            from withdraw_money import withdraw_amount
            withdraw_amount()
        elif choice == '4':
            from Balance_page import check_balance
            check_balance()
        elif choice == '5':
            from fraud_detector import show_alerts
            show_alerts()
        elif choice == '6':
            print("Thankyou for using our ATM service!")
            break
        else:
            print("Invalid choice! Please select a valid option (1-6) and try again.\n")

if __name__ == "__main__":
    main()

