# ATM Service by AURO TECH SOLUTIONS

## Overview

This is a simple ATM simulation implemented in Python. It allows users to create accounts, log in, deposit money, withdraw money, transfer money to other users, and view their transaction history.

## Features

1. **Create a New Account**: Users can create a new account by providing a user ID and a PIN.
2. **Login**: Users can log in to their account using their user ID and PIN.
3. **Deposit Money**: Logged-in users can deposit money into their account.
4. **Withdraw Money**: Logged-in users can withdraw money from their account, provided they have sufficient funds.
5. **Transfer Money**: Logged-in users can transfer money to other users' accounts, provided they have sufficient funds and the recipient exists.
6. **View Transaction History**: Logged-in users can view their transaction history to keep track of their deposits, withdrawals, and transfers.
7. **Logout**: Users can log out of their account.

## How to Use

1. **Run the Program**:
   - Execute the `main` function to start the ATM service.

2. **Main Menu**:
   - You will be greeted with a welcome message and three options:
     1. Create a new account
     2. Login
     3. Quit

3. **Create a New Account**:
   - Select option `1` and follow the prompts to enter your user ID and PIN. If the user ID is unique, your account will be created.

4. **Login**:
   - Select option `2` and enter your user ID and PIN. If the credentials are correct, you will be logged in.

5. **ATM Menu** (after login):
   - Once logged in, you will see the following options:
     1. Deposit: Enter the amount to deposit money into your account.
     2. Withdraw: Enter the amount to withdraw money from your account.
     3. Transfer: Enter the recipient's user ID and the amount to transfer money to another account.
     4. View Transaction History: View a list of all your transactions.
     5. Logout: Log out of your account.

6. **Quit**:
   - Select option `3` from the main menu to exit the program.

## Example Usage

```
Welcome to the ATM service provided by AURO TECH SOLUTIONS!!!!!!
1. Create a new account
2. Login
3. Quit
Enter your choice: 1
Enter user ID: user123
Enter PIN: 1234
User created.

1. Create a new account
2. Login
3. Quit
Enter your choice: 2
Enter user ID: user123
Enter PIN: 1234
Login successful.

ATM Menu:
1. Deposit
2. Withdraw
3. Transfer
4. View Transaction History
5. Logout
Enter your choice: 1
Enter deposit amount: 1000
Transaction successful.

ATM Menu:
1. Deposit
2. Withdraw
3. Transfer
4. View Transaction History
5. Logout
Enter your choice: 4
Transaction History:
Deposited Rupees 1000
```

## Note

- Make sure to input valid data for each operation.
- Ensure that you have sufficient funds for withdrawals and transfers.
- Transaction history is updated in real-time and can be viewed anytime after logging in.

Enjoy using the ATM service provided by AURO TECH SOLUTIONS!
