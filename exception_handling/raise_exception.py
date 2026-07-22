# raise_exception.py

balance = 5000

try:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    if amount > balance:
        raise Exception("Insufficient Balance.")

    balance -= amount

    print("Transaction Successful")
    print("Remaining Balance:", balance)

except Exception as error:
    print(error)