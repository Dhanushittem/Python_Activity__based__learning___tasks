n = int(input("Enter number of subjects: "))

total = 0
failed = 0

for i in range(1, n + 1):
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks")
        failed += 1

    elif marks >= 35:
        print("Pass")
        total += marks

    elif marks >= 30:
        print("Pass with grace marks")
        total += 35

    else:
        print("Fail")
        failed += 1
        total += marks

print("\nTotal Marks:", total)

if failed == 0:
    percentage = total / (n * 100) * 100
    print("Percentage:", percentage)

    if percentage >= 75:
        print("Distinction")
    elif percentage >= 60:
        print("First Class")
    elif percentage >= 50:
        print("Second Class")
    else:
        print("Pass")
else:
    print("Final Result: Fail")