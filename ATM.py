class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

class ATM:
    def __init__(self):
        self.users = {}

    def create_user(self, user_id, pin):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, pin)
            print("User created.")
        else:
            print("User already exists.")

    def login(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            print("Login successful.")
            return self.users[user_id]
        else:
            print("Invalid credentials.")
            return None

    def deposit(self, user, amount):
        user.balance += amount
        user.transaction_history.append("Deposited Rupees " + str(amount))

    def withdraw(self, user, amount):
        if user.balance >= amount:
            user.balance -= amount
            user.transaction_history.append("Withdrew Rupees " + str(amount))
        else:
            print("Insufficient funds")

    def transfer(self, user, recipient_id, amount):
        if recipient_id in self.users:
            recipient = self.users[recipient_id]
            if user.balance >= amount:
                user.balance -= amount
                recipient.balance += amount
                user.transaction_history.append("Transferred Rupees " + str(amount) + " to " + recipient_id)
            else:
                print("Insufficient funds")
        else:
            print("Recipient not found")

    def show_transaction_history(self, user):
        print("Transaction History:")
        for transaction in user.transaction_history:
            print(transaction)

def main():
    atm = ATM()

    while True:
        print("\nWelcome to the ATM service provided by AURO TECH SOLUTIONS!!!!!!")
        print("1. Create a new account")
        print("2. Login")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user_id = input("Enter user ID: ")
            pin = input("Enter PIN: ")
            atm.create_user(user_id, pin)
        elif choice == '2':
            user_id = input("Enter user ID: ")
            pin = input("Enter PIN: ")
            user = atm.login(user_id, pin)
            if user:
                while True:
                    print("\nATM Menu:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer")
                    print("4. View Transaction History")
                    print("5. Logout")

                    option = input("Enter your choice: ")

                    if option == '1':
                        amount = float(input("Enter deposit amount: "))
                        atm.deposit(user, amount)
                    elif option == '2':
                        amount = float(input("Enter withdrawal amount: "))
                        atm.withdraw(user, amount)
                    elif option == '3':
                        recipient_id = input("Enter recipient's user ID: ")
                        amount = float(input("Enter transfer amount: "))
                        atm.transfer(user, recipient_id, amount)
                    elif option == '4':
                        atm.show_transaction_history(user)
                    elif option == '5':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid option.")
        elif choice == '3':
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
