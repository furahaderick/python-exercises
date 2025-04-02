# Start
# - init principal_amount, time_in_years, rate, num_of_periods, final_amount to 0
# - prompt for principal_amount using "Enter the principal: "
# - prompt for the rate using "Enter the rate: "
# - prompt for the number of years using "Enter the number of years: "
# - prompt for the number of periods using "Enter the number of times the interest is compounded per year: "
# - final_amount = principal_amount * ((1 + (rate / 100) / num_of_periods) ** (num_of_periods * time_in_years))
# - display f"${principal_amount} invested at {rate}% for {time_in_years} years compounded {num_of_periods} times per years is ${final_amount}."
# End

principal_amount = 0
time_in_years = 0
rate = 0
num_of_periods = 0
final_amount = 0


class InvalidInputException(Exception):
    pass


def calculateCompoundInterest(principal, year_count, rate_of_interest, period_count):
    amount = principal * (
        (1 + (rate_of_interest / 100) / period_count) ** (period_count * year_count)
    )
    return amount


def checkPositiveNumber(num):
    if num < 0:
        raise InvalidInputException()
    else:
        return num


try:
    principal_amount = checkPositiveNumber(float(input("Enter the principal: ")))
    rate = checkPositiveNumber(float(input("Enter the rate: ")))
    time_in_years = checkPositiveNumber(float(input("Enter the number of years: ")))
    num_of_periods = checkPositiveNumber(
        int(input("Enter the number of times the interest is compounded per year: "))
    )

except ValueError:
    print("Please enter valid numbers.")
except InvalidInputException:
    print("Please enter positive numerals.")
else:
    final_amount = round(
        calculateCompoundInterest(
            principal_amount, time_in_years, rate, num_of_periods
        ),
        2,
    )
    print(
        f"${principal_amount} invested at {rate}% for {time_in_years} years compounded {num_of_periods} times per year is ${final_amount}."
    )
