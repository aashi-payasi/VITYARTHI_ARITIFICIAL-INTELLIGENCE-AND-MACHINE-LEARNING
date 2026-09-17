#login_page.py
#ATM system login page 

from account import account

def login(max_attempts: int=3) -> bool:

    for attempt in range(1, max_attempts + 1):
        pin = input("Enter your ATM Pin: ")
        if pin == account.get("pin"):
            print("Authentication Successful!\n")
            return True 
        else:
            remaining = max_attempts - attempt 
            if remaining > 0:
                print(f"Authentiation failed! {remaining} attempt(s) remaining.\n")
            else:
                print("Authentication failed. No remaining attempts left!\n")

    print("Your card has been temperarliy blocked due to multiple failed attepmts!")
    return False 

if __name__ == "__main__":
   login()
