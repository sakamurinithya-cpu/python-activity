#Library Fine Calculation
late_days = int(input("Enter number of late days: "))

if late_days < 0:
    print("Invalid number of days")
else:
    fine = late_days * 2
    print("Library Fine = ₹", fine)