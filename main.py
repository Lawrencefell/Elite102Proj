
import mysql.connector

class Account:
    def __init__(self, account_num, pin, balance):
        self.account_num = account_num
        self.pin = pin
        self.balance = balance

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
    query = ("INSERT INTO `elite102data`.`bankdeets` (AccountNumb, AccountName, Ballance, Pin, AccesLevel) VALUES (%s, %s, 0, %s, 0)")
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

    # Query to update the PIN
    query = ("UPDATE `elite102data`.`bankdeets` SET Pin = %s WHERE AccountNumb = %s AND Pin = %s")
    cursor.execute(query, (new_pin, account_num, current_pin))

    # Check if the PIN was updated successfully
    if cursor.rowcount > 0:
        print("PIN changed successfully.")
        connection.commit()
    else:
        print("Failed to change PIN. Make sure the current PIN is correct.")

    # Close cursor and connection
    cursor.close()
    connection.close()

def main_menu(user_account):
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
            pass
        elif choice == '3':
            # Implement deposit functionality
            pass
        elif choice == '4':
            # Implement withdrawal functionality
            pass
        elif choice == '5':
            # Implement delete account functionality
            pass
        elif choice == '6':
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please try again.")
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
        return Account(result[0], result[1], result[2])
    else:
        return None            

# Example usage:
login_or_create()
