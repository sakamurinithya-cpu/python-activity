#Retail Billing
name = input("Enter product name: ")
price = float(input("Enter price per item: "))
quantity = int(input("Enter quantity: "))

if price < 0 or quantity < 0:
    print("Invalid input")
else:
    total = price * quantity

    if total >= 1000:
        discount = total * 0.10
    else:
        discount = 0

    final_amount = total - discount

    print("Product:", name)
    print("Total Amount =", round(total, 2))
    print("Discount =", round(discount, 2))
    print("Final Amount =", round(final_amount, 2))