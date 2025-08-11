# Start
# - init name to ""
# - init greeting to ""
# - prompt for name using "What is your name? "
# - greeting = "Hello, {name}, nice to meet you"
# - Display greeting
# End

name = ""
greeting = ""

# name input
name = input("What is your name? ")

# Concatenation
greeting = f"Hello, {name}, nice to meet you."

# Output display
print(greeting)

# one-liner (without any variables)
print(f"Hello, {input('What is your name? ')}, nice to meet you.")
