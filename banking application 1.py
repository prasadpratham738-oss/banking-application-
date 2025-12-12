print("====== WELCOME TO PYTHON BANK ======")

accounts = {}

while True:
    print("\nWhat would you like to do?")
    print("1. Create New Account")
    print("2. Access Existing Account")
    print("3. Exit")
    main_choice = input("Enter your choice: ")

    if main_choice == "1":
        print("\n--- CREATE NEW BANK ACCOUNT ---")
        name = input("Enter your full name: ")
        age = int(input("Enter your age: "))
        phone = int(input("Enter your phone number: "))
        address = input("Enter your address: ")
        balance = float(input("Enter initial deposit amount: "))
        pin = input("Set a 4-digit PIN: ")

        account_number = 10000000000 + len(accounts) + phone

        accounts[account_number] = {
            "name": name,
            "age": age,
            "phone": phone,
            "address": address,
            "balance": balance,
            "pin": pin
        }

        print("\nAccount created successfully!")
        print("Account Number:", account_number)
        print("Balance:", balance)

    elif main_choice == "2":
        if len(accounts) == 0:
            print("\nNo accounts exist. Please create a new account first.")
        else:
            acc_number = int(input("Enter your account number: "))
            if acc_number in accounts:
                entered_pin = input("Enter your PIN: ")
                if entered_pin == accounts[acc_number]["pin"]:
                    print("\nLogin successful! Welcome,", accounts[acc_number]["name"])

                    continue_account = "y"
                    while continue_account.lower() == "y":
                        print("\n1. Deposit Money")
                        print("2. Withdraw Money")
                        print("3. Check Balance")
                        print("4. Update Phone")
                        print("5. Update Address")
                        print("6. Close Account")
                        print("7. Logout")
                        action = input("Enter your choice: ")

                        if action == "1":
                            amt = float(input("Enter amount to deposit: "))
                            if amt > 0:
                                accounts[acc_number]["balance"] += amt
                                print("Deposit successful! New balance:", accounts[acc_number]["balance"])
                            else:
                                print("Invalid amount!")

                        elif action == "2":
                            amt = float(input("Enter amount to withdraw: "))
                            if amt <= 0:
                                print("Invalid amount!")
                            elif amt > accounts[acc_number]["balance"]:
                                print("Insufficient balance!")
                            else:
                                accounts[acc_number]["balance"] -= amt
                                print("Withdrawal successful! New balance:", accounts[acc_number]["balance"])

                        elif action == "3":
                            print("Current balance:", accounts[acc_number]["balance"])

                        elif action == "4":
                            new_phone = input("Enter new phone number: ")
                            accounts[acc_number]["phone"] = new_phone
                            print("Phone updated successfully!")
                            print("updated phone number",accounts[acc_number]["phone"])

                        elif action == "5":
                            new_address = input("Enter new address: ")
                            accounts[acc_number]["address"] = new_address
                            print("Address updated successfully!")
                            print("updated address",accounts[acc_number]["address"])

                        elif action == "6":
                            confirm = input("Are you sure to close account? (yes/no): ").lower()
                            if confirm == "yes":
                                accounts.pop(acc_number)
                                print("Account closed successfully!")
                                break
                            else:
                                print("Account not closed.")

                        elif action == "7":
                            print("Logged out successfully.")
                            break

                        else:
                            print("Invalid choice! Enter 1-7.")

                        
                        if action != "7" and action != "6":
                            continue_account = input("\nDo you want to continue with your account? (y/n): ")
                            if continue_account.lower() != "y":
                                print("Logging out...")
                                break

                else:
                    print("Incorrect PIN! Access denied.")

            else:
                print("Account number not found!")

    elif main_choice == "3":
        print("Thank you for banking with Python Bank!")
        break

    else:
        print("Invalid choice! Enter 1, 2, or 3.")

