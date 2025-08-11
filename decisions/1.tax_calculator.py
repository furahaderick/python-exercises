# Start
# - init orderAmount, subtotal, tax, total, taxRate to 0
# - init state to ""
# - prompt for orderAmount using "What is the order amount? "
# - prompt for the state using "What is the state? "
# - IF state.lower() == "wi"
#   - taxRate = 5.5%
#  - subtotal = orderAmount.00, Print this if subtotal > 0 and tax != 0
#  - tax = orderAmount * 5.5%, Print this if subtotal > 0 and tax != 0
#  - total = subtotal + tax, Print this
# End

order_amount = 0
subtotal = 0
tax = 0
total = 0
state = ""

tax_rate = 0


try:
    order_amount = float(input("What is the order amount? "))
    state = input("What is the state? ")
except ValueError:
    print("Invalid numerals")
else:
    # Change the tax_rate according to state
    if state.lower() == "wi":
        tax_rate = 0.055

    subtotal = round(order_amount, 2)
    tax = order_amount * tax_rate
    total = subtotal + tax

    if subtotal > 0 and tax != 0:
        print(f"The subtotal is ${subtotal}.\nThe tax is ${tax}.")

    print(f"The total is ${total}.")
