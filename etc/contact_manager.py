# Python Contacts Manager


class InvalidChoiceException(Exception):
    pass


try:

    print("Python Contacts Manager")
    # Infinite loop
    while True:
        print("What do you want to do? (or 'q' to quit)")
        print("1. Register a contact")
        print("2. Get all your contact")
        print("3. Update a contact")
        print("4. Delete a contact")

        choice = input("Your choice > ")

        if choice == "q":
            print("Thanks for using Contacts Manager.")
            break
        else:
            choice = int(choice)

            if choice not in [1, 2, 3, 4]:
                raise InvalidChoiceException()

            if choice == 1:
                print("Register")
            elif choice == 2:
                print("Get All")
            elif choice == 3:
                print("Update One")
            else:
                print("Delete One")

except ValueError:
    print("Invalid Input Received")
except InvalidChoiceException:
    print("Invalid Choice Received")
