#Student Performance Analysis
marks = []

n = int(input("Enter number of subjects: "))

if n <= 0:
    print("Invalid number of subjects")
else:
    for i in range(n):
        mark = float(input("Enter marks: "))
        marks.append(mark)

    print("Highest Marks =", max(marks))
    print("Lowest Marks =", min(marks))
    print("Average Marks =", round(sum(marks) / n, 2))