# Start
# - init euros_amount, dollars_amount, euro_exchange_rate to 0
# - prompt for the euros with "How many euros are you exchanging? "
# - prompt for the euro_exchange_rate with "What is the exchange rate? "
# - dollars_amount = euros_amount * exchange_rate / 100
# - display f"{euros_amount} euros at an exchange rate of {euro_exchange_rate} is {dollars_amount} dollars."
# End

euros_amount = 0
dollars_amount = 0
euro_exchange_rate = 0

try:
    euros_amount = float(input("How many euros are you exchanging? "))
    euro_exchange_rate = float(input("What is the exchange rate? "))

    if euros_amount < 0 or euro_exchange_rate < 0:
        raise Exception("Use positive numbers.")

except ValueError:
    print("Please use valid numbers")
except Exception as error:
    print(f"Error: {error}")
else:
    dollars_amount = round(euros_amount * euro_exchange_rate / 100, 2)
    print(
        f"{euros_amount} euros at an exchange rate of {euro_exchange_rate} is {dollars_amount} dollars."
    )
