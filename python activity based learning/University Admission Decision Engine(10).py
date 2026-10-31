n = int(input("Enter number of students: "))

students = []

for i in range(1, n + 1):
    print("\nStudent", i)

    name = input("Enter student name: ")
    maths = int(input("Enter Maths marks: "))
    physics = int(input("Enter Physics marks: "))
    chemistry = int(input("Enter Chemistry marks: "))

    total = maths + physics + chemistry
    percentage = total / 3

    if maths >= 35 and physics >= 35 and chemistry >= 35 and percentage >= 60:
        print("Admission Eligible")
        students.append((name, percentage))
    else:
        print("Admission Not Eligible")

students.sort(key=lambda x: x[1], reverse=True)

print("\n----- ADMISSION RANK LIST -----")

if len(students) == 0:
    print("No eligible candidates")
else:
    for i, student in enumerate(students, 1):
        print("Rank:", i)
        print("Name:", student[0])
        print("Percentage:", round(student[1], 2))