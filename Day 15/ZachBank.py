import datetime
import random
import sys

# -------------------------
# Zach Bank Console App
# -------------------------

class ZachBankApp:
    accounts = {}  # in-memory account storage: account_number -> ZachBankApp instance

    def __init__(self, account_holder, account_number, pin, password="admin123"):
        self.bank_name = "ZACH BANK"
        self.account_holder = account_holder
        self.account_number = account_number
        self.pin = pin
        self.password = password
        self.balance = 50000.0
        self.history = []
        ZachBankApp.accounts[account_number] = self

    # --- Utilities ---
    def log_transaction(self, action):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"[{timestamp}] {action}")

    # --- Core features ---
    def deposit(self, amount, method="cash", details=None):
        if amount <= 0:
            print("\033[91mDeposit amount must be positive.\033[0m")
            return False
        self.balance += amount
        record = f"Deposited ₦{amount} via {method}"
        if details:
            record += f" ({details})"
        record += f". Balance: ₦{self.balance}"
        self.log_transaction(record)
        print(f"\033[92m✅ {record}\033[0m")
        return True

    def withdraw(self, amount, method="ATM", details=None):
        if amount <= 0:
            print("\033[91mWithdrawal amount must be positive.\033[0m")
            return False
        if amount > self.balance:
            print("\033[91m❌ Insufficient funds.\033[0m")
            return False
        self.balance -= amount
        record = f"Withdrew ₦{amount} via {method}"
        if details:
            record += f" ({details})"
        record += f". Balance: ₦{self.balance}"
        self.log_transaction(record)
        print(f"\033[93m✅ {record}\033[0m")
        return True

    def transfer_zachbank(self, amount, recipient_account, pin):
        if pin != self.pin:
            print("\033[91m❌ Incorrect transaction PIN.\033[0m")
            return False
        if amount <= 0:
            print("\033[91mTransfer amount must be positive.\033[0m")
            return False
        if amount > self.balance:
            print("\033[91m❌ Insufficient funds.\033[0m")
            return False
        if recipient_account not in ZachBankApp.accounts:
            print("\033[91m❌ Recipient account not found in Zach Bank.\033[0m")
            return False
        recipient = ZachBankApp.accounts[recipient_account]
        self.balance -= amount
        recipient.balance += amount
        record = f"Transferred ₦{amount} to Zach Bank account {recipient_account} ({recipient.account_holder}). Balance: ₦{self.balance}"
        self.log_transaction(record)
        print(f"\033[92m✅ {record}\033[0m")
        return True

    def transfer_other_bank(self, amount, recipient_account, recipient_bank, pin):
        if pin != self.pin:
            print("\033[91m❌ Incorrect transaction PIN.\033[0m")
            return False
        if amount <= 0:
            print("\033[91mTransfer amount must be positive.\033[0m")
            return False
        if amount > self.balance:
            print("\033[91m❌ Insufficient funds.\033[0m")
            return False
        self.balance -= amount
        record = f"Transferred ₦{amount} to {recipient_bank} account {recipient_account}. Balance: ₦{self.balance}"
        self.log_transaction(record)
        print(f"\033[92m✅ {record}\033[0m")
        return True

    def buy_airtime(self, amount, network, phone_number):
        if amount <= 0:
            print("\033[91mAmount must be positive.\033[0m")
            return False
        if amount > self.balance:
            print("\033[91m❌ Insufficient funds for airtime purchase.\033[0m")
            return False
        self.balance -= amount
        record = f"Airtime ₦{amount} purchased for {network} number {phone_number}. Balance: ₦{self.balance}"
        self.log_transaction(record)
        print(f"\033[92m✅ {record}\033[0m")
        return True

    def pay_bill(self, amount, bill_type):
        if amount <= 0:
            print("\033[91mAmount must be positive.\033[0m")
            return False
        if amount > self.balance:
            print("\033[91m❌ Insufficient funds for bill payment.\033[0m")
            return False
        self.balance -= amount
        record = f"Bill ₦{amount} paid for {bill_type}. Balance: ₦{self.balance}"
        self.log_transaction(record)
        print(f"\033[92m✅ {record}\033[0m")
        return True

    def check_balance(self):
        print("\n\033[96m📋 Account Details\033[0m")
        print(f"Bank: {self.bank_name}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ₦{self.balance}\n")

    def view_history(self):
        print("\n\033[95m📜 Transaction History\033[0m")
        if not self.history:
            print("No transactions yet.\n")
        else:
            for i, record in enumerate(self.history, 1):
                print(f"{i}. {record}")
            print()

    # --- Settings ---
    def reset_password(self, old_password, new_password):
        if old_password != self.password:
            print("\033[91m❌ Incorrect old password.\033[0m")
            return False
        self.password = new_password
        self.log_transaction("Password reset successfully.")
        print("\033[92m✅ Password reset successfully.\033[0m")
        return True

    def reset_pin(self, old_pin, new_pin):
        if old_pin != self.pin:
            print("\033[91m❌ Incorrect old PIN.\033[0m")
            return False
        if len(new_pin) != 4 or not new_pin.isdigit():
            print("\033[91m❌ PIN must be a 4-digit number.\033[0m")
            return False
        self.pin = new_pin
        self.log_transaction("Transaction PIN reset successfully.")
        print("\033[92m✅ Transaction PIN reset successfully.\033[0m")
        return True

    # --- Customer care ---
    def contact_customer_care(self):
        while True:
            clear_screen()
            print("\033[94m📞 Contact Customer Care\033[0m")
            print("1. Phone")
            print("2. Email")
            print("3. Live Chat")
            print("4. Visit Branch")
            print("5. Return")
            choice = input("Choose an option (1-5): ").strip()
            if choice == "1":
                print("📱 Call us at: +234-800-ZACH-BANK (Available 24/7)")
            elif choice == "2":
                print("📧 Send an email to: support@zachbank.com")
            elif choice == "3":
                print("💬 Live chat is available on our website: www.zachbank.com")
            elif choice == "4":
                print("🏦 Visit any ZACH BANK branch nationwide for assistance.")
            elif choice == "5":
                break
            else:
                print("\033[91mERROR INPUT, TRY AGAIN PLEASE.\033[0m")
            input("\nPress Enter to continue...")

# -------------------------
# Helper functions
# -------------------------

def clear_screen():
    print("\n" * 20)

def safe_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("\033[91mERROR INPUT, TRY AGAIN PLEASE.\033[0m")

def confirm_or_cancel():
    """
    Ask user to confirm or cancel. Return True to proceed, False to cancel.
    User should reply 'C' or 'c' to cancel and return to previous menu.
    Any other input proceeds.
    """
    choice = input("\nType 'C' to cancel and return, or press Enter to continue: ").strip()
    if choice.lower() == 'c':
        print("\033[93mAction cancelled. Returning to previous menu.\033[0m")
        return False
    return True

def post_transaction_menu():
    while True:
        print("\nWhat would you like to do next?")
        print("1. Go back to previous menu")
        print("2. Return to Main Menu")
        print("3. Make another transaction")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            return "back"
        elif choice == "2":
            return "main"
        elif choice == "3":
            return "repeat"
        elif choice == "4":
            print("\033[95mThank you for banking with ZACH BANK! Goodbye!\033[0m")
            sys.exit()
        else:
            print("\033[91m❌ Invalid choice, try again.\033[0m")

# -------------------------
# Account creation & login flows
# -------------------------

def open_account():
    clear_screen()
    print("🌟 OPEN A NEW ZACH BANK ACCOUNT 🌟")
    name = input("Enter full name: ").strip()
    while True:
        pin = input("Set a 4-digit PIN: ").strip()
        if len(pin) == 4 and pin.isdigit():
            break
        print("\033[91mPIN must be 4 digits.\033[0m")
    password = input("Set a login password: ").strip()
    # generate account number in the 10-digit 80xxxx... range
    while True:
        account_number = str(random.randint(8000000000, 8999999999))
        if account_number not in ZachBankApp.accounts:
            break
    account = ZachBankApp(name, account_number, pin, password)
    print(f"\n\033[92m✅ Account created successfully!\033[0m")
    print(f"Account Holder: {name}")
    print(f"Account Number: {account_number}")
    input("\nPress Enter to continue...")
    return account

def forgot_password():
    clear_screen()
    print("🔑 RESET PASSWORD")
    acc_num = input("Enter your account number: ").strip()
    pin = input("Enter your transaction PIN: ").strip()
    account = ZachBankApp.accounts.get(acc_num)
    if account and account.pin == pin:
        new_password = input("Enter new password: ").strip()
        # confirm before applying
        print("\nYou are about to reset your login password.")
        if confirm_or_cancel():
            account.password = new_password
            account.log_transaction("Password reset via Forgot Password flow.")
            print("\033[92m✅ Password reset successfully.\033[0m")
        else:
            print("\033[93mPassword reset cancelled.\033[0m")
    else:
        print("\033[91m❌ Account not found or incorrect PIN.\033[0m")
    input("\nPress Enter to continue...")

def show_logo():
    clear_screen()
    logo = [
        "  ________   _____   _   _    ____    _   _  _  __ ",
        " |__  / _ \\ |  __ \\ | \\ | |  / __ \\  | \\ | || |/ / ",
        "   / / | | || |__) ||  \\| | | |  | | |  \\| || ' /  ",
        "  / /| | | ||  _  / | . ` | | |  | | | . ` ||  <   ",
        " / /_| |_| || | \\ \\ | |\\  | | |__| | | |\\  || . \\  ",
        "/____|\\___/ |_|  \\_\\|_| \\_|  \\____/  |_| \\_||_|\\_\\ ",
        "               Z A C H   B A N K                    "
    ]
    for line in logo:
        print("\033[95m" + line + "\033[0m")
    print("\n")

def login_page():
    # Pre-create a sample account as requested
    if "8031528212" not in ZachBankApp.accounts:
        ZachBankApp("Zachariya Abdulfatai", "8031528212", pin="4321", password="4321")

    while True:
        show_logo()
        print("🌟 Welcome to Zach Bank 🌟")
        print("1. Login")
        print("2. Open Account")
        print("3. Forgot Password")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            acc_num = input("Enter account number: ").strip()
            password = input("Enter password: ").strip()
            account = ZachBankApp.accounts.get(acc_num)
            if account and account.password == password:
                print("\n\033[92mLogin successful. Welcome!\033[0m")
                input("\nPress Enter to continue...")
                return account
            else:
                print("\033[91m❌ Invalid login credentials.\033[0m")
                input("\nPress Enter to try again...")
        elif choice == "2":
            return open_account()
        elif choice == "3":
            forgot_password()
        elif choice == "4":
            print("\033[95mGoodbye!\033[0m")
            sys.exit()
        else:
            print("\033[91m❌ Invalid choice.\033[0m")
            input("\nPress Enter to continue...")

# -------------------------
# Deposit submenu flow
# -------------------------

def deposit_menu(account):
    while True:
        clear_screen()
        print("\033[96m--- DEPOSIT MENU ---\033[0m")
        print("1. Copy Account Number")
        print("2. Share Account Details")
        print("3. Cash Deposit (Fund via nearby merchants)")
        print("4. Top-up with Card")
        print("5. Bank USSD")
        print("6. Back to Main Menu")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            clear_screen()
            print("\033[94m📋 Copy Account Number\033[0m")
            print(f"Account Number: {account.account_number}")
            print("(Simulated copy to clipboard)")
            input("\nPress Enter to return to Deposit Menu...")
            continue

        elif choice == "2":
            clear_screen()
            print("\033[94m📤 Share Account Details\033[0m")
            print(f"Account Holder: {account.account_holder}")
            print(f"Account Number: {account.account_number}")
            print(f"Bank: {account.bank_name}")
            print("\n(You can share these details via your messaging app.)")
            input("\nPress Enter to return to Deposit Menu...")
            continue

        elif choice == "3":
            # Cash deposit via merchant
            while True:
                clear_screen()
                print("\033[94m🏧 Cash Deposit (Nearby Merchants)\033[0m")
                amount = safe_float_input("Enter cash deposit amount: ₦")
                details = input("Enter merchant name or reference (optional): ").strip()
                print("\nYou are about to deposit the amount to your Zach Bank account.")
                if not confirm_or_cancel():
                    input("\nPress Enter to return to Deposit Menu...")
                    break
                success = account.deposit(amount, method="Cash (Merchant)", details=details or None)
                if success:
                    action = post_transaction_menu()
                    if action == "repeat":
                        continue  # repeat cash deposit
                    elif action == "back":
                        break  # back to deposit menu
                    elif action == "main":
                        return  # return to main menu
                else:
                    input("\nPress Enter to try again...")
            continue

        elif choice == "4":
            # Top-up with card
            while True:
                clear_screen()
                print("\033[94m💳 Top-up with Card\033[0m")
                amount = safe_float_input("Enter card top-up amount: ₦")
                card_number = input("Enter card number (simulated): ").strip()
                card_name = input("Cardholder name: ").strip()
                print("\nYou are about to top-up your account with card.")
                if not confirm_or_cancel():
                    input("\nPress Enter to return to Deposit Menu...")
                    break
                # In a real app you'd validate card; here we simulate success
                success = account.deposit(amount, method="Card Top-up", details=f"Card {card_number[-4:]} {card_name}")
                if success:
                    action = post_transaction_menu()
                    if action == "repeat":
                        continue
                    elif action == "back":
                        break
                    elif action == "main":
                        return
                else:
                    input("\nPress Enter to try again...")
            continue

        elif choice == "5":
            # Bank USSD
            while True:
                clear_screen()
                print("\033[94m📲 Bank USSD Deposit\033[0m")
                amount = safe_float_input("Enter USSD deposit amount: ₦")
                ussd_code = input("Enter USSD code used (e.g. *123*1#): ").strip()
                print("\nYou are about to deposit via USSD.")
                if not confirm_or_cancel():
                    input("\nPress Enter to return to Deposit Menu...")
                    break
                success = account.deposit(amount, method="USSD", details=ussd_code)
                if success:
                    action = post_transaction_menu()
                    if action == "repeat":
                        continue
                    elif action == "back":
                        break
                    elif action == "main":
                        return
                else:
                    input("\nPress Enter to try again...")
            continue

        elif choice == "6":
            return  # back to main menu

        else:
            print("\033[91mERROR INPUT, TRY AGAIN PLEASE.\033[0m")
            input("\nPress Enter to continue...")

# -------------------------
# Withdraw flow (enhanced)
# -------------------------

def withdraw_menu(account):
    while True:
        clear_screen()
        print("\033[96m--- WITHDRAW MENU ---\033[0m")
        print("1. Withdraw via Zach Bank Merchants")
        print("2. Withdraw with Zach Bank Card (ATM / POS)")
        print("3. Back to Main Menu")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            # Withdraw via merchant: transfer to merchant wallet, user collects cash from merchant
            while True:
                clear_screen()
                print("\033[94m🏧 Withdraw via Zach Bank Merchants\033[0m")
                print("Find a nearby Zach Bank merchant, then send funds to their merchant wallet.")
                amount = safe_float_input("Enter amount to send to merchant (₦): ")
                merchant_account = input("Enter merchant Zach Bank account number: ").strip()
                pin = input("Enter transaction PIN to authorize: ").strip()
                # allow cancel before processing
                print("\nYou are about to send funds to the merchant for cash withdrawal.")
                if not confirm_or_cancel():
                    input("\nPress Enter to return to Withdraw Menu...")
                    break
                # Validate merchant exists and is a ZachBank account
                if merchant_account not in ZachBankApp.accounts:
                    print("\033[91m❌ Merchant account not found in Zach Bank.\033[0m")
                    input("\nPress Enter to try again...")
                    continue
                success = account.transfer_zachbank(amount, merchant_account, pin)
                if success:
                    print("\nPlease present the transaction reference to the merchant to collect cash.")
                    action = post_transaction_menu()
                    if action == "repeat":
                        continue
                    elif action == "back":
                        break
                    elif action == "main":
                        return
                else:
                    input("\nPress Enter to try again...")
            continue

        elif choice == "2":
            # Withdraw with card: simulate card-linked withdrawal at ATM/POS
            while True:
                clear_screen()
                print("\033[94m💳 Withdraw with Zach Bank Card (ATM / POS)\033[0m")
                print("You can withdraw cash from any ATM or POS using your Zach Bank card.")
                amount = safe_float_input("Enter withdrawal amount: ₦")
                card_number = input("Enter your Zach Bank card number (simulated): ").strip()
                atm_location = input("Enter ATM/POS location (optional): ").strip()
                pin = input("Enter transaction PIN to authorize: ").strip()
                print("\nYou are about to authorize a card withdrawal.")
                if not confirm_or_cancel():
                    input("\nPress Enter to return to Withdraw Menu...")
                    break
                # Simulate card validation by checking PIN only (no real card linking)
                if pin != account.pin:
                    print("\033[91m❌ Incorrect transaction PIN.\033[0m")
                    input("\nPress Enter to try again...")
                    continue
                success = account.withdraw(amount, method="Card (ATM/POS)", details=f"Card {card_number[-4:]} at {atm_location or 'Unknown location'}")
                if success:
                    print("\nTransaction approved. Use your card at the ATM/POS to collect cash.")
                    action = post_transaction_menu()
                    if action == "repeat":
                        continue
                    elif action == "back":
                        break
                    elif action == "main":
                        return
                else:
                    input("\nPress Enter to try again...")
            continue

        elif choice == "3":
            return

        else:
            print("\033[91mERROR INPUT, TRY AGAIN PLEASE.\033[0m")
            input("\nPress Enter to continue...")

# -------------------------
# Transfer flows
# -------------------------

def transfer_zachbank_flow(account):
    while True:
        clear_screen()
        print("\033[96m--- TRANSFER (ZACH BANK) ---\033[0m")
        amount = safe_float_input("Enter transfer amount: ₦")
        recipient_account = input("Enter recipient Zach Bank account number: ").strip()
        pin = input("Enter transaction PIN: ").strip()
        print("\nYou are about to transfer funds to another Zach Bank account.")
        if not confirm_or_cancel():
            input("\nPress Enter to return to Transfer Menu...")
            return
        success = account.transfer_zachbank(amount, recipient_account, pin)
        if success:
            action = post_transaction_menu()
            if action == "repeat":
                continue
            elif action in ("back", "main"):
                return
        else:
            input("\nPress Enter to try again...")

def transfer_other_bank_flow(account):
    while True:
        clear_screen()
        print("\033[96m--- TRANSFER (OTHER BANKS) ---\033[0m")
        amount = safe_float_input("Enter transfer amount: ₦")
        recipient_account = input("Enter recipient account number: ").strip()
        recipient_bank = input("Enter recipient bank: ").strip()
        pin = input("Enter transaction PIN: ").strip()
        print("\nYou are about to transfer funds to another bank.")
        if not confirm_or_cancel():
            input("\nPress Enter to return to Transfer Menu...")
            return
        success = account.transfer_other_bank(amount, recipient_account, recipient_bank, pin)
        if success:
            action = post_transaction_menu()
            if action == "repeat":
                continue
            elif action in ("back", "main"):
                return
        else:
            input("\nPress Enter to try again...")

# -------------------------
# Airtime & Bills flows
# -------------------------

def airtime_flow(account):
    while True:
        clear_screen()
        print("\033[96m--- BUY AIRTIME ---\033[0m")
        amount = safe_float_input("Enter airtime amount: ₦")
        network = input("Enter network (MTN/GLO/Airtel/9mobile): ").strip()
        phone_number = input("Enter recipient phone number: ").strip()
        print("\nYou are about to purchase airtime.")
        if not confirm_or_cancel():
            input("\nPress Enter to return to Airtime Menu...")
            return
        success = account.buy_airtime(amount, network, phone_number)
        if success:
            action = post_transaction_menu()
            if action == "repeat":
                continue
            elif action in ("back", "main"):
                return
        else:
            input("\nPress Enter to try again...")

def bill_payment_flow(account):
    while True:
        clear_screen()
        print("\033[96m--- BILL PAYMENT ---\033[0m")
        amount = safe_float_input("Enter bill amount: ₦")
        bill_type = input("Enter bill type (Electricity/Water/Internet): ").strip()
        print(f"\nYou are about to pay {bill_type} bill.")
        if not confirm_or_cancel():
            input("\nPress Enter to return to Bill Menu...")
            return
        success = account.pay_bill(amount, bill_type)
        if success:
            action = post_transaction_menu()
            if action == "repeat":
                continue
            elif action in ("back", "main"):
                return
        else:
            input("\nPress Enter to try again...")

# -------------------------
# Settings flow
# -------------------------

def settings_menu(account):
    while True:
        clear_screen()
        print("\033[96m--- SETTINGS ---\033[0m")
        print("1. Reset Login Password")
        print("2. Reset Transaction PIN")
        print("3. Back")
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            old_password = input("Enter old password: ").strip()
            new_password = input("Enter new password: ").strip()
            print("\nYou are about to reset your login password.")
            if confirm_or_cancel():
                account.reset_password(old_password, new_password)
            else:
                print("\033[93mPassword reset cancelled.\033[0m")
            input("\nPress Enter to continue...")
        elif choice == "2":
            old_pin = input("Enter old PIN: ").strip()
            new_pin = input("Enter new 4-digit PIN: ").strip()
            print("\nYou are about to reset your transaction PIN.")
            if confirm_or_cancel():
                account.reset_pin(old_pin, new_pin)
            else:
                print("\033[93mPIN reset cancelled.\033[0m")
            input("\nPress Enter to continue...")
        elif choice == "3":
            return
        else:
            print("\033[91mERROR INPUT, TRY AGAIN PLEASE.\033[0m")
            input("\nPress Enter to continue...")

# -------------------------
# Main menu
# -------------------------

def main_menu(account):
    while True:
        clear_screen()
        print("\033[95m" + "="*50 + "\033[0m")
        print("\033[95m🌟 Welcome to ZACH BANK 🌟\033[0m")
        print("\033[95m" + "="*50 + "\033[0m")
        print(f"\033[94mAccount Holder: {account.account_holder}\033[0m")
        print(f"\033[94mAccount Number: {account.account_number}\033[0m")
        print(f"\033[94mCurrent Balance: ₦{account.balance}\033[0m\n")

        print("--- MAIN MENU ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer to another Zach Bank")
        print("4. Transfer to other Banks")
        print("5. Buy Airtime")
        print("6. Bill Payments")
        print("7. View Transaction History")
        print("8. Contact Customer Care")
        print("9. Settings")
        print("10. Exit")

        choice = input("Choose an option (1-10): ").strip()

        if choice == "1":
            deposit_menu(account)

        elif choice == "2":
            withdraw_menu(account)

        elif choice == "3":
            transfer_zachbank_flow(account)

        elif choice == "4":
            transfer_other_bank_flow(account)

        elif choice == "5":
            airtime_flow(account)

        elif choice == "6":
            bill_payment_flow(account)

        elif choice == "7":
            clear_screen()
            account.view_history()
            input("\nPress Enter to return to Main Menu...")

        elif choice == "8":
            account.contact_customer_care()

        elif choice == "9":
            settings_menu(account)

        elif choice == "10":
            print("\033[95mThank you for banking with ZACH BANK! Goodbye!\033[0m")
            break

        else:
            print("\033[91mERROR INPUT, TRY AGAIN PLEASE.\033[0m")
            input("\nPress Enter to continue...")

# -------------------------
# Run the app
# -------------------------

if __name__ == "__main__":
    user_account = login_page()
    main_menu(user_account)
