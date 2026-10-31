balance = float(input("Enter initial balance: "))
n = int(input("Enter number of transactions: "))

total_deposit = 0
total_withdrawal = 0

for i in range(1, n + 1):
    print("\n1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter your choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")

    elif choice == 1:
        balance += amount
        total_deposit += amount
        print("Amount deposited successfully")

    elif choice == 2:
        if amount > 10000:
            print("Withdrawal limit exceeded")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            total_withdrawal += amount
            print("Withdrawal successful")

    else:
        print("Invalid transaction")

print("\n----- ATM SUMMARY -----")
print("Final Balance:", balance)
print("Total Deposits:", total_deposit)
print("Total Withdrawals:", total_withdrawal)