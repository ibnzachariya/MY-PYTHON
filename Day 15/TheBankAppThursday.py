import datetime

class BankAccount:
    def __init__(self, account_holder, account_number, pin):
        self.bank_name = "ZACH BANK"
        self.account_holder = account_holder
        self.account_number = account_number
        self.pin = pin
        self.balance = 50000.0  # Initial balance in Naira
        self.history = []       # Transaction history list

    def log_transaction(self, action):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"[{timestamp}] {action}")

    def deposit(self, amount, method="cash", recipient_account=None, recipient_bank=None):
        if amount <= 0:
            print("\033[91mDeposit amount must be positive.\033[0m")
            return
        self.balance += amount
        record = f"Deposited ₦{amount} via {method} to {recipient_bank} account {recipient_account}. Balance: ₦{self.balance}"
        self.log_transaction(record)
        print(f"\033[92m✅ {record}\033[0m")

    def withdraw(self, amount, method="ATM", recipient_account=None, recipient_bank=None):
        if amount <= 0:
            print("\033[91mWithdrawal amount must be positive.\033[0m")
            return
        if amount > self.balance:
            print("\033[91m❌ Insufficient funds.\033[0m")
            return

        self.balance -= amount
        if method.lower() == "transfer":
            record = f"Transferred ₦{amount} to {recipient_bank} account {recipient_account}. Balance: ₦{self.balance}"
        else:
            record = f"Withdrew ₦{amount} via {method}. Balance: ₦{self.balance}"

        self.log_transaction(record)
        print(f"\033[93m✅ {record}\033[0m")

    def check_balance(self):
        print("\n\033[96m📋 Account Details\033[0m")
        print(f"Bank: {self.bank_name}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ₦{self.balance}\n")

    def buy_airtime(self, amount, network="MTN", phone_number=None):
        if amount > self.balance:
            print("\033[91m❌ Insufficient funds for airtime purchase.\033[0m")
            return
        self.balance -= amount
        record = f"Airtime ₦{amount} purchased for {network} number {phone_number}. Balance: ₦{self.balance}"
        self.log_transaction(record)
        print(f"\033[92m✅ {record}\033[0m")

    def pay_bill(self, amount, bill_type="Electricity"):
        if amount > self.balance:
            print("\033[91m❌ Insufficient funds for bill payment.\033[0m")
            return
        self.balance -= amount
        record = f"Bill ₦{amount} paid for {bill_type}. Balance: ₦{self.balance}"
        self.log_transaction(record)
        print(f"\033[92m✅ {record}\033[0m")

    def view_history(self):
        print("\n\033[95m📜 Transaction History\033[0m")
        if not self.history:
            print("No transactions yet.\n")
        else:
            for i, record in enumerate(self.history, 1):
                print(f"{i}. {record}")
            print()

    def contact_customer_care(self):
        while True:
            print("\n\033[94m📞 Contact Customer Care\033[0m")
            print("How would you like to reach us?")
            print("1. Phone")
            print("2. Email")
            print("3. Live Chat")
            print("4. Visit Branch")
            print("5. Return to Main Menu")

            choice = input("Choose an option (1-5): ")
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


def safe_float_input(prompt):
    """Helper function to safely get a float input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\033[91mERROR INPUT, TRY AGAIN PLEASE.\033[0m")


def post_operation_menu():
    while True:
        print("\nWhat would you like to do next?")
        print("1. Return to Main Menu")
        print("2. Go Back (repeat last action)")
        print("3. Cancel / Exit App")

        choice = input("Choose an option (1-3): ")
        if choice == "1":
            return "main"
        elif choice == "2":
            return "back"
        elif choice == "3":
            print("\033[95mThank you for banking with ZACH BANK! Goodbye!\033[0m")
            exit()
        else:
            print("\033[91mERROR INPUT, TRY AGAIN PLEASE.\033[0m")


def main():
    account = BankAccount("Abdulfatai Zachariya", "123456789", pin="4321")

    # PIN login loop
    while True:
        entered_pin = input("Enter your 4-digit PIN to access ZACH BANK: ")
        if entered_pin == account.pin:
            break
        else:
            print("\033[91mERROR INPUT, TRY AGAIN PLEASE.\033[0m")

    # Welcome screen
    print("\n" * 20)
    print("\033[95m" + "="*50)
    print("🌟 Welcome to ZACH BANK 🌟")
    print("="*50 + "\033[0m")
    print(f"\033[94mAccount Holder: {account.account_holder}\033[0m")
    print(f"\033[94mAccount Number: {account.account_number}\033[0m")
    print(f"\033[94mCurrent Balance: ₦{account.balance}\033[0m\n")

    # Main menu loop
    while True:
        print("\n" * 20)
        print("--- MAIN MENU ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Buy Airtime")
        print("5. Bill Payments")
        print("6. View Transaction History")
        print("7. Contact Customer Care")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")

        if choice == "1":
            amount = safe_float_input("Enter amount to deposit: ₦")
            method = input("Enter method (transfer/ATM/cash): ")
            recipient_account = input("Enter recipient account number: ")
            recipient_bank = input("Enter recipient bank: ")
            account.deposit(amount, method, recipient_account, recipient_bank)
            if post_operation_menu() == "back":
                account.deposit(amount, method, recipient_account, recipient_bank)

        elif choice == "2":
            amount = safe_float_input("Enter amount to withdraw: ₦")
            method = input("Enter method (ATM/cash/transfer): ")
            if method.lower() == "transfer":
                recipient_account = input("Enter recipient account number: ")
                recipient_bank = input("Enter recipient bank: ")
                account.withdraw(amount, method, recipient_account, recipient_bank)
                if post_operation_menu() == "back":
                    account.withdraw(amount, method, recipient_account, recipient_bank)
            else:
                account.withdraw(amount, method)
                if post_operation_menu() == "back":
                    account.withdraw(amount, method)

        elif choice == "3":
            account.check_balance()
            post_operation_menu()

        elif choice == "4":
            amount = safe_float_input("Enter airtime amount: ₦")
            network = input("Enter network (MTN/GLO/Airtel/9mobile): ")
            phone_number = input("Enter recipient phone number: ")
            account.buy_airtime(amount, network, phone_number)
            if post_operation_menu() == "back":
                account.buy_airtime(amount, network, phone_number)

        elif choice == "5":
            amount = safe_float_input("Enter bill amount: ₦")
            bill_type = input("Enter bill type (Electricity/Water/Internet): ")
            account.pay_bill(amount, bill_type)
            if post_operation_menu() == "back":
                account.pay_bill(amount, bill_type)

        elif choice == "6":
            account.view_history()
            post_operation_menu()

        elif choice == "7":
            account.contact_customer_care()
            post_operation_menu()

        elif choice == "8":
            print("\033[95mThank you for banking with ZACH BANK! Goodbye!\033[0m")
            break

        else:
            print("\033[91mERROR INPUT, TRY AGAIN PLEASE.\033[0m")


# Run the app
main()
