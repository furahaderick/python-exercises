# Start
# init username to ""
# init password to ""
# prompt for username with "Enter username: "
# Filter users for user with the exact username
#   - if found: continue
#   - if not found: display "User not found"
# prompt for password with "What is the password?: "
# check if user's password is the same as the password provided
#   - if pwds match: display "You're welcome {username}"
#   - if pwds dont match: display "I don't know you"
# End


class UserNotFoundError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


users = [
    {"username": "furahaderick", "password": "test@123"},
    {"username": "maxtyga", "password": "m@xTyga1"},
    {"username": "aidaan", "password": "@richGuy"},
    {"username": "derio", "password": "@rio1"},
]


def find_user_by_username(username):
    user_match = {}
    for user in users:
        if user["username"] == username:
            user_match = user
            return user_match
    return None


username = ""
password = ""
user_match = {}

try:
    username = input("Enter username: ")
    user_match = find_user_by_username(username)

    if user_match == None:
        raise UserNotFoundError()

    password = input("What is the password?: ")

    if user_match["password"] != password:
        raise InvalidCredentialsError()

except UserNotFoundError:
    print("I don't know you (username)")
except InvalidCredentialsError:
    print("I don't know you (password)")
else:
    print(f"You're welcome, {user_match['username']}")
