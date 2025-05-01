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


class Constants(Enum):
    ACCEPTED_AGE = 16


age_input = 0

try:
    age_input = int(input("What is your age? "))
except ValueError:
    print("Invalid input received")
else:
    print(
        f"{'You are not old enough to drive' if age_input < Constants.ACCEPTED_AGE.value else 'You are old enough to drive'}"
    )
