#Attendence Calculation
total_classes = int(input("Enter total classes: "))
attended = int(input("Enter classes attended: "))

if total_classes <= 0 or attended < 0 or attended > total_classes:
    print("Invalid input")
else:
    percentage = (attended / total_classes) * 100

    print("Attendance Percentage =", round(percentage, 2), "%")

    if percentage >= 75:
        print("Eligible for examination")
    else:
        print("Not eligible for examination")