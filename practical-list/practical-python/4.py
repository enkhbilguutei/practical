# . WAP that accepts a character and performs the following:
# a. print whether the character is a letter or numeric digit or a special character
# b. if the character is a letter, print whether the letter is uppercase or lowercase
# c. if the character is a numeric digit, prints its name in text (e.g., if input is 9,
# output is NINE)
# Get input character from user

char = input("Enter a character: ")

# Check if character is a letter, a digit or a special character
if char.isalpha():
    # Check if letter is uppercase or lowercase
    if char.isupper():
        print("The character is an uppercase letter.")
    else:
        print("The character is a lowercase letter.")
elif char.isdigit():
    # Convert digit to text and print
    digit_text = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    print("The character is a digit, and its name in text is:", digit_text[int(char)])
else:
    print("The character is a special character.")
