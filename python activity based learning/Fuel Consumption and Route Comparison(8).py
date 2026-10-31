n = int(input("Enter number of vehicles: "))

distance = float(input("Enter journey distance in km: "))
fuel_price = float(input("Enter fuel price per litre: "))
reserve = float(input("Enter reserve fuel required in litres: "))

lowest_cost = float('inf')
best_vehicle = ""

for i in range(1, n + 1):
    print("\nVehicle", i)

    name = input("Enter vehicle name: ")
    mileage = float(input("Enter mileage (km/litre): "))

    if mileage <= 0:
        print("Invalid mileage")
        continue

    fuel = distance / mileage
    total_fuel = fuel + reserve
    cost = total_fuel * fuel_price

    print("Fuel Required:", round(total_fuel, 2), "litres")
    print("Journey Cost: Rs.", round(cost, 2))

    if cost < lowest_cost:
        lowest_cost = cost
        best_vehicle = name

print("\n----- ROUTE COMPARISON -----")

if best_vehicle != "":
    print("Lowest Cost Vehicle:", best_vehicle)
    print("Lowest Journey Cost: Rs.", round(lowest_cost, 2))
else:
    print("No feasible vehicle found")