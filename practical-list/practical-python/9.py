# #WAP to read a file and
# m. Print the total number of characters, words and lines in the file.
# n. Calculate the frequency of each character in the file. Use a variable of dictionary
# type to maintain the count.
# o. Print the words in reverse order.
# p. Copy even lines of the file to a file named ‘File1’ and odd lines to another
# file named ‘File2’.

def file_operations(file_name):
    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read the contents of the file
        file_contents = file.read()

        # Count the number of characters, words, and lines in the file
        num_characters = len(file_contents)
        num_words = len(file_contents.split())
        num_lines = file_contents.count('\n') + 1

        # Create a dictionary to store the frequency of each character in the file
        char_freq = {}
        for char in file_contents:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

        # Print the total number of characters, words, and lines in the file
        print(f"Total number of characters: {num_characters}")
        print(f"Total number of words: {num_words}")
        print(f"Total number of lines: {num_lines}")

        # Print the words in reverse order
        words = file_contents.split()
        reversed_words = ' '.join(words[::-1])
        print(f"Words in reverse order: {reversed_words}")

        # Copy even and odd lines to separate files
        with open('File1', 'w') as file1, open('File2', 'w') as file2:
            lines = file_contents.split('\n')
            for i, line in enumerate(lines):
                if i % 2 == 0:
                    file1.write(line + '\n')
                else:
                    file2.write(line + '\n')

        # Print the frequency of each character in the file
        print("Frequency of each character:")
        for char, freq in char_freq.items():
            print(f"'{char}': {freq}")

file_operations('input_file.txt')
