entry = int(input("Enter entry hour (0-23): "))
exit = int(input("Enter exit hour (0-23): "))

vehicle = input("Enter vehicle type (car/bike): ").lower()

if entry < 0 or entry > 23 or exit < 0 or exit > 23:
    print("Invalid time")

elif vehicle != "car" and vehicle != "bike":
    print("Invalid vehicle type")

else:
    if exit < entry:
        hours = (24 - entry) + exit
    else:
        hours = exit - entry

    if hours == 0:
        hours = 1

    if vehicle == "car":
        rate = 30
    else:
        rate = 15

    fee = hours * rate

    if fee > 200:
        fee = 200

    if hours > 24:
        fee += 100

    print("Parking Duration:", hours, "hours")
    print("Vehicle Type:", vehicle)
    print("Parking Fee: Rs.", fee)