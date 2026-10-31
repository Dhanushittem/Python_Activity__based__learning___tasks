n = int(input("Enter number of products: "))
budget = float(input("Enter your total budget: "))

total = 0

for i in range(1, n + 1):
    print("\nProduct", i)

    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity < 0:
        print("Invalid input")
        continue

    amount = price * quantity

    if amount >= 1000:
        discount = amount * 0.10
    else:
        discount = 0

    final_price = amount - discount
    total += final_price

    print("Product:", name)
    print("Total Amount:", amount)
    print("Discount:", discount)
    print("Final Price:", final_price)

print("\nTotal Shopping Amount:", total)

if total <= budget:
    print("Shopping is within budget")
else:
    print("Budget Exceeded")
    print("Extra Amount Required:", total - budget)

print("Remaining Budget:", max(0, budget - total))