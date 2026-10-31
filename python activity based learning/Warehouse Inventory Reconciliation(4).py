n = int(input("Enter number of products: "))

for i in range(1, n + 1):
    print("\nProduct", i)

    opening = int(input("Enter opening stock: "))
    incoming = int(input("Enter incoming quantity: "))
    dispatched = int(input("Enter dispatched quantity: "))
    closing = int(input("Enter actual closing stock: "))

    expected = opening + incoming - dispatched

    print("Expected Stock:", expected)

    if closing == expected:
        print("Stock Reconciled")
    else:
        print("Stock Discrepancy:", closing - expected)

    if closing < 10:
        print("Replenishment Required:", 10 - closing)
    else:
        print("Stock is Sufficient")

print("\nInventory Reconciliation Completed")