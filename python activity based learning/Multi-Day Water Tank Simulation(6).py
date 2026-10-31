capacity = float(input("Enter tank capacity in litres: "))
water = float(input("Enter initial water level: "))
n = int(input("Enter number of days: "))
threshold = float(input("Enter required water level: "))

if capacity <= 0 or water < 0 or water > capacity or threshold < 0 or threshold > capacity:
    print("Invalid input")

else:
    for i in range(1, n + 1):
        inflow = float(input("Enter water inflow: "))
        outflow = float(input("Enter water outflow: "))

        water = water + inflow - outflow

        if water > capacity:
            print("Overflow detected")
            water = capacity

        elif water < 0:
            print("Water shortage detected")
            water = 0

        print("Day", i, "Water Level:", water)

        if water >= threshold:
            print("Threshold reached on Day", i)
            break

    print("Final Water Level:", water)