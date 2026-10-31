n = int(input("Enter number of subjects: "))
m = int(input("Enter number of examinations: "))

for i in range(1, n + 1):
    print("\nSubject", i)

    marks = []

    for j in range(1, m + 1):
        score = int(input("Enter exam " + str(j) + " marks: "))
        marks.append(score)

    improvement = marks[-1] - marks[0]

    print("First Exam Marks:", marks[0])
    print("Last Exam Marks:", marks[-1])

    if improvement > 0:
        print("Performance Improved by:", improvement)
    elif improvement < 0:
        print("Performance Declined by:", abs(improvement))
    else:
        print("Performance Remained Same")

    if all(score < 35 for score in marks):
        print("Weak Subject")
    else:
        print("Performance is Satisfactory")

print("\nPerformance Analysis Completed")