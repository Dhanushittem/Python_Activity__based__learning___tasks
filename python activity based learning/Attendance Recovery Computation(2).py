attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes conducted: "))
threshold = float(input("Enter required attendance percentage: "))

if attended < 0 or total <= 0 or attended > total or threshold < 0 or threshold > 100:
    print("Invalid input")
else:
    percentage = (attended / total) * 100
    print("Current Attendance:", round(percentage, 2), "%")

    if percentage >= threshold:
        print("Attendance Eligible")
        print("Additional Classes Required: 0")
    else:
        classes = 0
        while ((attended + classes) / (total + classes)) * 100 < threshold:
            classes += 1

        print("Attendance Not Eligible")
        print("Additional Consecutive Classes Required:", classes)
        print("Final Attendance:", round(((attended + classes) / (total + classes)) * 100, 2), "%")