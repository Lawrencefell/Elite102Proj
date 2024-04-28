
import mysql.connector

class Account:
    def __init__(self, account_num,AccountName, balance, pin, AccesLevel):
        self.account_num = account_num
        self.AccountName = AccountName
        self.balance = balance
        self.pin = pin
        self.AccesLevel = AccesLevel

def LogIn(account_num, pin):
    # Connect to the database
    connection = mysql.connector.connect(user="LawAdmin", database='elite102data', password="FYuUZamsY8pIr+tMfFGRS5H1rKUbq9i/MT6etRMtSfeqGXIXk0uW9lYV+UQ4boefWqd0wjQu5APXrUFxfCHvzXM65rTv8qtTkpXsO/Vk13rY3k")
    cursor = connection.cursor()

    # Query to check if the account exists and the PIN matches
    query = ("SELECT * FROM `elite102data`.`bankdeets` WHERE AccountNumb = %s AND pin = %s")
    cursor.execute(query, (account_num, pin))

    # Fetch the first row (if any)
    result = cursor.fetchone()

    # Close cursor and connection
    cursor.close()
    connection.close()

    # Return True if account exists and PIN matches, False otherwise
    return result is not None

def create_account(account_num, account_name, pin):
    # Connect to the database
    connection = mysql.connector.connect(user="LawAdmin", database='elite102data', password="FYuUZamsY8pIr+tMfFGRS5H1rKUbq9i/MT6etRMtSfeqGXIXk0uW9lYV+UQ4boefWqd0wjQu5APXrUFxfCHvzXM65rTv8qtTkpXsO/Vk13rY3k")
    cursor = connection.cursor()

    # Insert new account details into the database
    query = ("INSERT INTO `elite102data`.`bankdeets` (AccountNumb, AccountName, ballence, Pin, AccesLevel) VALUES (%s, %s, 0, %s, 0)")
    cursor.execute(query, (account_num, account_name, pin))

    # Commit changes and close cursor and connection
    connection.commit()
    cursor.close()
    connection.close()

    print("Account created successfully.")

def is_valid_pin(pin):
    # Check if the pin has exactly 4 digits and consists only of numeric characters
    if len(pin) != 4 or not pin.isdigit():
        return False

    # If all conditions pass, return True
    return True
    
def change_pin(account_num, current_pin, new_pin):
    # Connect to the database
    if not is_valid_pin(new_pin):
        print("Invalid PIN. PIN must be 4 digits(0-9), and contain no spaces, letters, or special characters.")
        return

    connection = mysql.connector.connect(user="LawAdmin", database='elite102data', password="FYuUZamsY8pIr+tMfFGRS5H1rKUbq9i/MT6etRMtSfeqGXIXk0uW9lYV+UQ4boefWqd0wjQu5APXrUFxfCHvzXM65rTv8qtTkpXsO/Vk13rY3k")
    cursor = connection.cursor()

    try:
        # Check if the current PIN matches the one stored in the database
        check_query = ("SELECT COUNT(*) FROM `elite102data`.`bankdeets` WHERE AccountNumb = %s AND Pin = %s")
        cursor.execute(check_query, (account_num, current_pin))
        result = cursor.fetchone()
        if result[0] == 0:
            print("Failed to change PIN. The current PIN is incorrect.")
            return

        # Update the PIN
        update_query = ("UPDATE `elite102data`.`bankdeets` SET Pin = %s WHERE AccountNumb = %s")
        cursor.execute(update_query, (new_pin, account_num))

        # Check if the PIN was updated successfully
        if cursor.rowcount > 0:
            print("PIN changed successfully.")
            connection.commit()
        else:
            print("Failed to change PIN.")
    except mysql.connector.Error as err:
        print(f"Error updating PIN: {err}")
    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()

def deposit(account_num, amount):
    # Connect to the database
    connection = mysql.connector.connect(user="LawAdmin", database='elite102data', password="FYuUZamsY8pIr+tMfFGRS5H1rKUbq9i/MT6etRMtSfeqGXIXk0uW9lYV+UQ4boefWqd0wjQu5APXrUFxfCHvzXM65rTv8qtTkpXsO/Vk13rY3k")
    cursor = connection.cursor()

    # Query to check if the PIN matches
    query = ("SELECT * FROM `elite102data`.`bankdeets` WHERE AccountNumb = %s ")
    cursor.execute(query, (account_num,))

    # Fetch the first row (if any)
    result = cursor.fetchone()

    # If PIN matches and the withdrawal amount is valid
    if result is not None:
        ballence = result[2]
        if amount >= 0:
            # Query to update the balance
            query = ("UPDATE `elite102data`.`bankdeets` SET ballence = ballence + %s WHERE AccountNumb = %s")
            cursor.execute(query, (amount, account_num))
            print("deposit of $", amount, "successful.")
            connection.commit()
        else:
            print("invalid amount.")
    cursor.close()
    connection.close()

def withdraw(account_num, pin, amount):
    # Connect to the database
    connection = mysql.connector.connect(user="LawAdmin", database='elite102data', password="FYuUZamsY8pIr+tMfFGRS5H1rKUbq9i/MT6etRMtSfeqGXIXk0uW9lYV+UQ4boefWqd0wjQu5APXrUFxfCHvzXM65rTv8qtTkpXsO/Vk13rY3k")
    cursor = connection.cursor()

    # Query to check if the PIN matches
    query = ("SELECT * FROM `elite102data`.`bankdeets` WHERE AccountNumb = %s AND Pin = %s")
    cursor.execute(query, (account_num, pin))

    # Fetch the first row (if any)
    result = cursor.fetchone()

    # If PIN matches and the withdrawal amount is valid
    if result is not None:
        balance = result[2]
        if amount <= balance:
            # Query to update the balance
            query = ("UPDATE `elite102data`.`bankdeets` SET ballence = ballence - %s WHERE AccountNumb = %s")
            cursor.execute(query, (amount, account_num))
            print("Withdrawal of $", amount, "successful.")
            connection.commit()
        else:
            print("Insufficient funds.")
    else:
        print("PIN verification failed. Please try again.")

    # Close cursor and connection
    cursor.close()
    connection.close()
def listAll():
  # Connect to the database
    connection = mysql.connector.connect(user="LawAdmin", database='elite102data', password="FYuUZamsY8pIr+tMfFGRS5H1rKUbq9i/MT6etRMtSfeqGXIXk0uW9lYV+UQ4boefWqd0wjQu5APXrUFxfCHvzXM65rTv8qtTkpXsO/Vk13rY3k")
    cursor = connection.cursor()

    # Query to check if the account exists and the PIN matches
    query = ("SELECT AccountNumb, AccountName, ballence FROM `elite102data`.`bankdeets` ")
    cursor.execute(query, multi=True)

    # Fetch the first row (if any)
    result = cursor.fetchall()

    # Check if result is not None before iterating
    if result:
        for row in result:
            print(row)

    # Close cursor and connection
    cursor.close()
    connection.close()
def viewAccount(ViewNumb):
  # Connect to the database
    connection = mysql.connector.connect(user="LawAdmin", database='elite102data', password="FYuUZamsY8pIr+tMfFGRS5H1rKUbq9i/MT6etRMtSfeqGXIXk0uW9lYV+UQ4boefWqd0wjQu5APXrUFxfCHvzXM65rTv8qtTkpXsO/Vk13rY3k")
    cursor = connection.cursor()

    try:
        # Query to check if the account exists and the PIN matches
        query = ("SELECT AccountNumb, AccountName, ballence FROM `elite102data`.`bankdeets` WHERE AccountNumb = %s")
        cursor.execute(query, (ViewNumb,))
        
        # Fetch the first row (if any)
        result = cursor.fetchone()
        
        if result:
            print("Account Number:", result[0])
            print("Account Name:", result[1])
            print("Balance:", result[2])
        else:
            print("Account not found.")
    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()
    # Close cursor and connection
    cursor.close()
    connection.close()
def freezeAccount(accountNumb,accountName):
  # Connect to the database
    connection = mysql.connector.connect(user="LawAdmin", database='elite102data', password="FYuUZamsY8pIr+tMfFGRS5H1rKUbq9i/MT6etRMtSfeqGXIXk0uW9lYV+UQ4boefWqd0wjQu5APXrUFxfCHvzXM65rTv8qtTkpXsO/Vk13rY3k")
    cursor = connection.cursor()

    # Query to check if the account exists and the PIN matches
    query = ("SELECT * FROM `elite102data`.`bankdeets` WHERE AccountNumb = %s AND AccountName = %s")
    cursor.execute(query, (accountNumb,accountName))
    result = cursor.fetchone()
        # Fetch the first row (if any)
    query = ("UPDATE `elite102data`.`bankdeets` SET AccesLevel = 2 WHERE AccountNumb = %s AND AccountName = %s")
    cursor.execute(query, (accountNumb,  accountName))
    print("freeze of ", accountName, "successful.")
    connection.commit()
    # Close cursor and connection
    cursor.close()
    connection.close()
def main_menu(user_account):
  if user_account.AccesLevel == 0:
    while True:
        print("\nMain Menu:")
        print("1. Check Balance")
        print("2. Change PIN")
        print("3. Deposit")
        print("4. Withdrawal")
        print("5. Delete Account")
        print("6. Log Out")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Implement check balance functionality
            print("Your balance is:", user_account.balance)
        elif choice == '2':
            # Implement change PIN functionality
            current_pin = input("Enter your current PIN: ")
            new_pin1 = input("Enter your new PIN: ")
            new_pin2 = input("Enter your new PIN again: ")

            if new_pin1 == new_pin2:
                change_pin(user_account.account_num, current_pin, new_pin1)
            else:
                print("New PINs do not match. Please try again.")
            
        elif choice == '3':
            deposit_amount = input("Enter the amount you wish to deposit (format: 1234.56): ")
            try:
                amount = float(deposit_amount)
                if amount <= 0:
                    print("Amount must be greater than zero.")
                else:
                    deposit(user_account.account_num, amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number. please enter only the amount")
        elif choice == '4':
            
            # Withdrawal functionality
            withdraw_amount = input("Enter the amount you wish to withdraw (format: 1234.56): ")
            try:
                amount = float(withdraw_amount)
                if amount <= 0:
                    print("Amount must be greater than zero.")
                elif amount > user_account.balance:
                    print("Withdrawal amount exceeds available balance.")
                else:
                    pin = input("Enter your PIN for verification: ")
                    withdraw(user_account.account_num, pin, amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number. please enter only the amount")
        elif choice == '5':
            # Implement delete account functionality
            pass
        elif choice == '6':
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please try again.")
  if user_account.AccesLevel == 1:
      while True:
        print("\nAdmin Menu:")
        print("1. list all") ##will not include pins
        print("2. view account")## will access an individual account
        print("3. place freeze")## may be added if time permits
        print("4. deactivate accounts")## will remove an account from the data
        print("5. Log Out")
        choice = input("Enter your choice: ")
        if choice == '1':
          listAll()
          pass
        elif choice == '2':
          print("\nwhat acount whould you like to view")
          ViewNumb = input("Account Number: ")
          viewAccount(ViewNumb)
          pass
        elif choice == '3':
          print("\nFreeze account")
          accountNumb = input("Enter Account Number: ")
          accountName = input("Enter Account Name: ")
          print(f'are you sure you wish to freeze.\n account Name: {accountName} \n account Number: {accountNumb}')
          freezeAccount(accountNumb,accountName)
          pass
        elif choice == '4':
          pass
        elif choice == '5':
          print("quiting all")
          quit()
    
def login_or_create():
    while True:    
        choice = input("Do you want to (1) log into an existing account or (2) create a new account? Enter 1 or 2: ")
        if choice == '1':
            # Log into an existing account
            account_num_input = input("Enter account number: ")
            pin_input = input("Enter PIN: ")

            if LogIn(account_num_input, pin_input):
                print("Login successful.")
                # Implement further actions for logged in users
                user_account = get_account_details(account_num_input)
                main_menu(user_account)
            else:
                print("Account does not exist or PIN does not match.")
        elif choice == '2':
            # Create a new account
            account_num = input("Enter new account number: ")
            account_name = input("Enter account name: ")
            pin = input("Set PIN for the new account: ")
            create_account(account_num, account_name, pin)
            print("Account created successfully.")
            # Cache the newly created account
            user_account = Account(account_num, account_name, 0, pin, 0)
            main_menu(user_account)
            # Implement further actions for newly created accounts
        else:
            print("Invalid choice.")

def get_account_details(account_num):
    # Connect to the database
    connection = mysql.connector.connect(user="LawAdmin", database='elite102data', password="FYuUZamsY8pIr+tMfFGRS5H1rKUbq9i/MT6etRMtSfeqGXIXk0uW9lYV+UQ4boefWqd0wjQu5APXrUFxfCHvzXM65rTv8qtTkpXsO/Vk13rY3k")
    cursor = connection.cursor()

    # Query to fetch account details
    query = ("SELECT * FROM `elite102data`.`bankdeets` WHERE AccountNumb = %s")
    cursor.execute(query, (account_num,))

    # Fetch the account details
    result = cursor.fetchone()

    # Close cursor and connection
    cursor.close()
    connection.close()

    if result:
        # Create an Account object and return it
        return Account(result[0], result[1], result[2],result[3],result[4] )
    else:
        return None            

# Encapsulate main code in a function
def main():
    login_or_create()

# Call main function if script is executed directly
if __name__ == "__main__":
    main()
