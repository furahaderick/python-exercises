# Start
# init weight to 0
# init MALE_ALCOHOL_RATIO to 0.73 and FEMALE_ALCOHOL_RATIO to 0.66 and VOLUME_PER_DRINK to 12
# init gender to ""
# init drinks_count to 0
# init alcohol_content_per_drink to 0
# init hours_since_last_drink to 0
# init total_alcohol_volume to 0
# init bac_value to 0
# prompt for weight using "Enter your weight: "
# prompt for gender using "Enter your gender: "
# prompt for hours_since_last_drink using "How many hours have passed since last drink? "
# prompt for drinks_count using "How many drinks did you have then? "
# prompt for alcohol_content_per_drink using "What was the alcohol % in those drinks? "
# total_alcohol_volume = (VOLUME_PER_DRINK * alcohol_content_per_drink) * drinks_count
# IF gender == "M":
#   bac = (total_alcohol_volume * 5.14 / weight * MALE_ALCOHOL_RATIO) - (0.015 * hours_since_last_drink)
# ELSE IF gender == "F":
#   bac = (total_alcohol_volume * 5.14 / weight * FEMALE_ALCOHOL_RATIO) - (0.015 * hours_since_last_drink)
# ELSE
#   display "Invalid gender"
#
# End

from enum import Enum


class Constants(Enum):
    MALE_ALCOHOL_RATIO = 0.73
    FEMALE_ALCOHOL_RATIO = 0.66

    # A beer drink's volume in ounces (oz)
    DRINK_VOL_BEER = 12


class InvalidGenderException(Exception):
    pass


weight = 0
gender = ""
drinks_count = 0
alcohol_content_per_drink = 0
hours_since_last_drink = 0
total_alcohol_volume = 0
bac_value = 0

try:
    weight = float(input("Enter your weight: "))
    gender = input("What is your gender (M/F)?: ").capitalize()

    if gender not in ["M", "F"]:
        raise InvalidGenderException()

    hours_since_last_drink = int(input("How many hours have passed since last drink? "))
    drinks_count = int(input("How many drinks did you have then? "))
    alcohol_content_per_drink = int(input("What was the alcohol % in those drinks? "))
    total_alcohol_volume = (
        Constants.DRINK_VOL_BEER.value * (alcohol_content_per_drink / 100)
    ) * drinks_count

    if gender == "m":
        bac_value = (
            total_alcohol_volume * 5.14 / weight * Constants.MALE_ALCOHOL_RATIO.value
        ) - (0.015 * hours_since_last_drink)
    else:
        bac_value = (
            total_alcohol_volume * 5.14 / weight * Constants.FEMALE_ALCOHOL_RATIO.value
        ) - (0.015 * hours_since_last_drink)

except ValueError:
    print("Invalid input received")
except InvalidGenderException:
    print("Invalid gender input. Use 'm' or 'f' only")
else:
    bac_value = round(bac_value, 2)
    print(f"Your BAC is {bac_value}")
    if bac_value <= 0.08:
        print("It is not legal for you to drive")
    else:
        print("You can drive")
