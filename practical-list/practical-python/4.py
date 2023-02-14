# . WAP that accepts a character and performs the following:
# a. print whether the character is a letter or numeric digit or a special character
# b. if the character is a letter, print whether the letter is uppercase or lowercase
# 44 | P a g e
# c. if the character is a numeric digit, prints its name in text (e.g., if input is 9,
# output is NINE)

def char_info(c):
    """Prints information about the given character"""
    if c.isalpha():
        if c.isupper():
            print(f"{c} is an uppercase letter.")
        else:
            print(f"{c} is a lowercase letter.")
    elif c.isdigit():
        print(f"{c} is a numeric digit ({digit_to_text(c)}).")
    else:
        print(f"{c} is a special character.")

def digit_to_text(d):
    """Converts a digit character to its corresponding text representation"""
    text = {
        '0': 'ZERO',
        '1': 'ONE',
        '2': 'TWO',
        '3': 'THREE',
        '4': 'FOUR',
        '5': 'FIVE',
        '6': 'SIX',
        '7': 'SEVEN',
        '8': 'EIGHT',
        '9': 'NINE'
    }
    return text.get(d)

# Example usage
char_info('a')  # lowercase letter
char_info('B')  # uppercase letter
char_info('5')  # numeric digit
char_info('$')  # special character
