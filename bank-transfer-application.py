transfer_limit = 5
transfer_count = 0
transfer_fee = 3.50
low_balance_mode = 50.0

def bank_transfer(checking_balance=float, savings_balance=float):
    global transfer_count

    program_running = True

    name_input = input("Enter your name:\n").capitalize().strip()

    print(f"""\nWelcome to CD Bank, {name_input}! 
    You have been directed to the Balance Transfer Portal.""")


    while program_running:

        # From Account
        while True:
            from_account = input("\nTransferring from \033[34mChecking\033[0m or \033[32mSavings\033[0m?\n").capitalize().strip()

            if from_account in ["Checking", "Savings"]:
                break
            print("Entry invalid. Please enter \"\033[32mSavings\033[0m\" or \"\033[32mChecking\033[0m\" for proper assistance.")

        # To Account
        while True:
            to_account = input("\nTransferring to \033[34mChecking\033[0m or \033[32mSavings?\033[0m\n").capitalize().strip()
            if to_account not in ["Checking", "Savings"]:
                print("Entry invalid. Please enter \"\033[32mSavings\033[0m\" or \"\033[32mChecking\033[0m\" for proper assistance.")
            elif to_account == from_account:
                print("Entry invalid. You cannot transfer to the same account that is being transferred from.")
            else:
                break

        while True:
            try:
                print("\n\033[31m* If your transfer count exceeds the limit of 5 uses, you will be charged a $3.50 fee. *")
                transfer_input = float(input(f"\033[0mEnter the amount you want to transfer from {from_account}: $"))
                if transfer_input <= 0:
                    print("Entry invalid. Amount must be greater than 0.")

                transfer_amount = transfer_input
                if transfer_count >= transfer_limit:
                    transfer_amount += transfer_fee
                    print("You have reached the transfer limit. Additional transfers will be $3.50")

                if from_account == "Checking" and transfer_amount > checking_balance:
                    print(f"Entry invalid. You have selected an amount greater than amount in Checking.")
                    continue

                if from_account == "Savings" and transfer_amount > savings_balance:
                    print(f"Entry invalid. You have selected an amount greater than amount in Savings.")
                    continue

                break

            except ValueError:
                print("Entry invalid. Please enter a number")

        if from_account == "Checking":
            checking_balance -= transfer_amount
            savings_balance += transfer_input
        else:
            savings_balance -= transfer_amount
            checking_balance += transfer_input

        transfer_count += 1

        # TEXT TURNS RED AFTER BALANCE EXCEEDS LOW BALANCE MODE
        if checking_balance <= low_balance_mode:
            checking_display = f"\033[31m{checking_balance:,.2f}\033[0m"
        else:
            checking_display = f"{checking_balance:,.2f}"

        if savings_balance <= low_balance_mode:
            savings_display = f"Low Balance Mode Activated: \033[31m{savings_balance:,.2f}\033[0m"
        else:
            savings_display = f"{savings_balance:,.2f}"

        # TEXT TURNS RED AFTER EXCEEDING TRANSFER LIMIT
        if transfer_count > transfer_limit:
            transfer_display = f"\033[31m{transfer_count}\033[0m"
        else:
            transfer_display = f"{transfer_count}"

        print(f"""
\033[32mTransfer sucessful\033[0m.
- Checking Balance: ${checking_display}
- Savings Balance: ${savings_display}
- Transfers used: {transfer_display}/5
""")

        additional_transfer = input("Do you want to make another transfer?\n").capitalize().strip()
        if additional_transfer != "Yes":
            program_running = False
            print("Thanks for using CD Bank!")

if __name__ == "__main__":

    bank_transfer(765.0, 4325.0)