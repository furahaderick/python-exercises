# Start
# - init principal_amount, rate, time_in_years, interest_amount, amount_per_year final_amount to 0
# - prompt for principal_amount using "Enter the principal: "
# - prompt for the rate using "Enter the rate of interest: "
# - prompt for time_in_years using "Enter the number of years: "
# - amount_per_year = principal_amount * rate / 100
# - interest_amount = amount_per_year * time_in_years
# - final_amount = principal_amount + interest_amount
# - display f"After {time_in_years} at {rate}%, the investment will be worth ${final_amount}."
# End

principal_amount = 0
rate = 0
time_in_years = 0
amount_per_year = 0
interest_amount = 0
final_amount = 0


class InvalidInputException(Exception):
    pass


def calculateSimpleInterest(principal, rate_of_interest, years):
    amount_after_one_year = principal * rate_of_interest / 100
    amount_after_years = amount_after_one_year * years
    return {
        "amount_per_year": amount_after_one_year,
        "interest_amount": amount_after_years,
    }


try:
    principal_amount = float(input("Enter the principal: $"))
    rate = float(input("Enter the rate of interest: "))
    time_in_years = int(input("Enter the number of years: "))

    if principal_amount < 0 or rate < 0 or time_in_years < 0:
        raise InvalidInputException()

except ValueError:
    print("Please enter valid numbers.")
except InvalidInputException:
    print("Received invalid numerals.")
else:
    simple_interest_info = calculateSimpleInterest(
        principal_amount, rate, time_in_years
    )

    amount_per_year = simple_interest_info["amount_per_year"]
    interest_amount = simple_interest_info["interest_amount"]

    final_amount = round(principal_amount + interest_amount, 3)

    print(
        f"At {rate}%:\nAfter 1 year: ${amount_per_year}\nAfter {time_in_years} years, the investment will be worth ${final_amount}"
    )
