# Start
# - Set accepted_age to 16
# - init age_input to 0
# - prompt for the age using "What is your age? "
# - IF age_input < accepted_age THEN
#   - display "You're not old enough to legally drive."
# - ELSE
#   - display "You're old enough to legally drive."
# End

from enum import Enum


class NegativeAgeInput(Exception):
    pass


class Constants(Enum):
    ACCEPTED_AGE = 16


age_input = 0

# try:
#     age_input = int(input("What is your age? "))
#     if age_input < 0:
#         raise NegativeAgeInput()
# except ValueError:
#     print("Invalid input received")
# except NegativeAgeInput:
#     print("You can't use negative numbers")
# else:
#     print(
#         f"{'You are not old enough to drive' if age_input < Constants.ACCEPTED_AGE.value else 'You are old enough to drive'}"
#     )


# Challenge:
# Instead of hard-coding the driving age in your program
# logic, research driving ages for various countries and
# create a lookup table for the driving ages and countries.
# Prompt for the age, and display which countries the
# user can legally drive in.

COUNTRIES_DRIVING_AGES = [
    {"country_name": "Rwanda", "accepted_age": 18},
    {"country_name": "Tanzania", "accepted_age": 18},
    {"country_name": "Morocco", "accepted_age": 18},
    {"country_name": "USA", "accepted_age": 16},
    {"country_name": "France", "accepted_age": 17},
    {"country_name": "Cameroon", "accepted_age": 16},
    {"country_name": "Uganda", "accepted_age": 18},
]

accepted_countries = []
unaccepted_countries = []

try:
    age_input = int(input("What is your age?: "))
    if age_input < 0:
        raise NegativeAgeInput()

except ValueError:
    print("Only numerals please")
except NegativeAgeInput:
    print("You can't use negative numbers")
else:

    for country in COUNTRIES_DRIVING_AGES:
        if country["accepted_age"] > age_input:
            unaccepted_countries.append(country["country_name"])
        else:
            accepted_countries.append(country["country_name"])

    if len(accepted_countries) > 0:
        print("You can drive in:")
        for country in accepted_countries:
            print(f"- {country}")
    else:
        print("You can't drive in any country as far as we know")

    if len(unaccepted_countries) > 0:
        print("You can't drive in:")
        for country in unaccepted_countries:
            print(f"- {country}")
    else:
        print("Yep, You can drive in all countries (as far as we know)")
