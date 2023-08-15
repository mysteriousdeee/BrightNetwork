# Set default balance
balance = 5000

# Create a default pin
pin = 1234

# Get users pin and store in variable
user_pin = int(input("Kindly enter your 4 digit PIN code: "))

# Check if the entered PIN matches the user's PIN
if user_pin == pin:
    # (Extension 1): If the PIN matches, prompt the user if they'd like to withdraw or deposit
    options = {
        1: "Withdraw",
        2: "Deposit"
    }

 # Display ATM options
for key, value in options.items():
    print(f"{key}. {value}")

# Take choice from user among the options
choice = int(input("Enter your choice (1/2): "))

if choice in options:
    if choice == 1:
        # Option 1: Withdraw
        amount = int(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. Your new balance is ${balance}")
        else:
            print("Insufficient funds!")
    elif choice == 2:
        # Option 2: Deposit
        amount = int(input("Enter the amount to deposit: "))
        balance += amount
        print(f"Deposit successful. Your new balance is ${balance}")
    else:
        print("Invalid choice")
else:
    print("PIN incorrect. Access denied.")
