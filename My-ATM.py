# Simple ATM Machine Simulation
user = {
    'pin': 1234,
    'balance': 50000
}

def withdraw_cash():
    amount = int(input("Enter the amount to withdraw: "))
    if amount > user['balance']:
        print("Insufficient balance!")
    else:
        user['balance'] -= amount
        print(f"{amount} withdrawn successfully. Remaining balance: {user['balance']}")

def deposit_cash():
    amount = int(input("Enter the amount to deposit: "))
    user['balance'] += amount
    print(f"{amount} deposited successfully. New balance: {user['balance']}")

def balance_enquiry():
    print(f"Your current balance is: {user['balance']}")

def atm_menu():
    print("Welcome to the ATM")
    pin = int(input("Please enter your 4-digit PIN: "))
    if pin == user['pin']:
        while True:
            print("\nATM Menu:")
            print("1. Withdraw Cash")
            print("2. Deposit Cash")
            print("3. Balance Enquiry")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                withdraw_cash()
            elif choice == 2:
                deposit_cash()
            elif choice == 3:
                balance_enquiry()
            elif choice == 4:
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Incorrect PIN. Please try again.")

atm_menu()
