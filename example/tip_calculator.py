bill_amount = 0
tip_rate = 0
tip = 0
total_amount = 0

bill_amount = float(input("Enter bill amount: $ "))
tip_rate = float(input("Enter tip percentage: "))

tip = round(bill_amount * (tip_rate / 100), 2)

total_amount = bill_amount + tip

print(f"Tip: ${tip}")
print(f"Total: ${total_amount}")
