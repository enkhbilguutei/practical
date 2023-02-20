# #WAP to read a file and
# m. Print the total number of characters, words and lines in the file.
# n. Calculate the frequency of each character in the file. Use a variable of dictionary
# type to maintain the count.
# o. Print the words in reverse order.
# p. Copy even lines of the file to a file named ‘File1’ and odd lines to another
# file named ‘File2’.
# Function to count characters, words, and lines in a file

def count_chars_words_lines(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
        num_chars = len(data)
        num_words = len(data.split())
        num_lines = data.count('\n') + 1
    return num_chars, num_words, num_lines

# Function to calculate the frequency of each character in a file
def char_frequency(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
        freq_dict = {}
        for char in data:
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    return freq_dict

# Function to print the words in reverse order
def reverse_words(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
        words = data.split()
        rev_words = ' '.join(words[::-1])
    return rev_words

# Function to copy even lines to File1 and odd lines to File2
def copy_lines(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        even_lines = []
        odd_lines = []
        for i, line in enumerate(lines):
            if i % 2 == 0:
                even_lines.append(line)
            else:
                odd_lines.append(line)
    with open('File1', 'w') as f1:
        f1.writelines(even_lines)
    with open('File2', 'w') as f2:
        f2.writelines(odd_lines)

# Take input from user
file_name = input("Enter the file name: ")

# Call the functions and print the results
num_chars, num_words, num_lines = count_chars_words_lines(file_name)
print("Number of characters:", num_chars)
print("Number of words:", num_words)
print("Number of lines:", num_lines)

freq_dict = char_frequency(file_name)
print("Frequency of each character:", freq_dict)

rev_words = reverse_words(file_name)
print("Words in reverse order:", rev_words)

copy_lines(file_name)
print("Even lines copied to File1, odd lines copied to File2")


# This code assumes that the input file exists and is readable. The analyzle_file function reads the file and returns the requested information. The write_lines_to_file function writes the specified lines to the specified file, either marking them as even or odd. The split_lines function splits the lines in the input file into two files: File1 for even lines and file 2 for odd lines. 
