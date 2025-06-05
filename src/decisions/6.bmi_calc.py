# Start
# init bmi_value, height, weight to 0
# prompt for height using "..."
# prompt for weight using "..."
# bmi_value = calculate_bmi(height, weight)
# if bmi < 18.5:
#   - print("Underweight")
# else if bmi >= 18.5 and bmi <= 25:
#   - print("Normal weight")
# else:
#   - print("Overweight")
# End

bmi_value = 0
height = 0
weight = 0


class CrazyCountingException(Exception):
    pass


def calculate_bmi(h, w):
    bmi = (w / (h * h)) * 703
    return bmi


try:
    height = float(input("Enter your height in inches: "))
    weight = float(input("Enter your weight in pounds: "))

    if height <= 0 or weight <= 0:
        raise CrazyCountingException()
except ValueError:
    print("Invalid numerals...")
except CrazyCountingException:
    print("You must be joking...")
else:
    bmi_value = calculate_bmi(height, weight)
    bmi_value = round(bmi_value, 1)

    print(f"Your BMI is {bmi_value}")

    if bmi_value < 18.5:
        print("You are underweight. You should see a doctor.")
    elif bmi_value >= 18.5 and bmi_value <= 25:
        print("You are within the ideal weight range.")
    else:
        print("You are overweight. You should see a doctor.")
