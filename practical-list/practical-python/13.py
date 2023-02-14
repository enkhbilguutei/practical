# WAP to accept a name from a user. Raise and handle appropriate exception(s) if the text entered
# by the user contains digits and/or special characters.

def get_valid_name():
    while True:
        try:
            name = input("Enter your name: ")
            if not name.isalpha():
                raise ValueError("Invalid characters found in name. Please enter only alphabets.")
            return name
        except ValueError as e:
            print(e)

name = get_valid_name()
print("Your name is:", name)
