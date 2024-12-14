# -*- coding: utf-8 -*-
"""problems1file handling.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1r1Sd2F7FQYHVw5VdkBL_WaBu1vVvzjqu

read from a file
"""

file=open("/content/data.txt","r")
content=file.read()
print(content)
file.close()

"""append to a file"""

file=open("/content/data.txt","a")
file.write("this is an append line.\n")
file.close()

"""count lines in a file"""

with open("/content/data.txt","r") as file:
  line_count=sum(1 for line in file)

  print(f"the number of lines in data.txt is : {line_count}")

"""count words in a file"""

with open("/content/data.txt","r") as file:
  content=file.read()
  words=content.split()
  words_count=len(words)
  print(f"the number of words in data.txt is : {words_count} words.")

"""copy file contents"""

with open("/content/data.txt","r") as source_file, open("copy.txt","w") as destruction_file:
       content=source_file.read()

"""check if file exists"""

# prompt: check if file exists

import os

file_exists = os.path.exists("/content/data.txt")

if file_exists:
    print("The file exists.")
else:
    print("The file does not exist.")

"""read file line by line"""

# prompt: read file line by line

with open("/content/data.txt", "r") as file:
    for line in file:
        print(line, end="") # end="" prevents extra newline

"""search for a word in a file"""

# prompt: search for a word in a file

import os

def search_word_in_file(filepath, word):
    """Searches for a specific word in a file and returns the line numbers where it's found."""
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            results = []
            for i, line in enumerate(lines):
                if word in line:
                    results.append(i + 1)  # Line numbers start from 1
            return results
    except FileNotFoundError:
        return f"Error: File '{filepath}' not found."

# Example usage:
filepath = "/content/data.txt"  # Replace with the actual file path
word_to_search = "append"  # The word to search for
line_numbers = search_word_in_file(filepath, word_to_search)

if isinstance(line_numbers, str):  # Check for error message
    print(line_numbers)
elif line_numbers:
    print(f"The word '{word_to_search}' was found on lines: {', '.join(map(str, line_numbers))}")
else:
    print(f"The word '{word_to_search}' was not found in the file.")

"""write a list to a file"""

# prompt: write a list to a file

my_list = ["apple", "banana", "cherry"]

with open("my_list.txt", "w") as f:
  for item in my_list:
    f.write("%s\n" % item)

"""reverse file contents"""

# prompt: reverse file contents

with open("/content/data.txt", "r") as file:
    lines = file.readlines()

with open("/content/data.txt", "w") as file:
    for line in reversed(lines):
        file.write(line)

"""file statistics"""

# prompt: file statistics

import os

def file_stats(filepath):
    """Provides statistics about a file."""
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)

        file_size = os.path.getsize(filepath)  # Get file size in bytes

        return {
            "lines": num_lines,
            "words": num_words,
            "characters": num_chars,
            "size_bytes": file_size,
        }

    except FileNotFoundError:
        return "Error: File not found."


# Example usage
filepath = "/content/data.txt"  # Replace with the actual file path
stats = file_stats(filepath)

if isinstance(stats, str):  # Check for error message
    print(stats)
else:
    print(f"File Statistics for '{filepath}':")
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value}")

"""merge two files"""

# prompt: merge two files

def merge_files(file1_path, file2_path, output_path):
    """Merges two files into a new file."""
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(output_path, 'w') as outfile:
            outfile.write(file1.read())
            outfile.write(file2.read())
        print(f"Files '{file1_path}' and '{file2_path}' merged into '{output_path}' successfully.")
    except FileNotFoundError:
        print("Error: One or both of the input files were not found.")

# Example usage:
file1_path = "/content/data.txt"  # Replace with the path to your first file
file2_path = "copy.txt"  # Replace with the path to your second file
output_path = "merged_file.txt"  # Replace with the desired output file path

merge_files(file1_path, file2_path, output_path)

"""count occurrences of a word"""

# prompt: count occurrences of a word

def count_word_occurrences(filepath, word):
    """Counts the occurrences of a specific word in a file."""
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            words = content.lower().split()  # Convert to lowercase for case-insensitive counting
            return words.count(word.lower())
    except FileNotFoundError:
        return f"Error: File '{filepath}' not found."

# Example usage
filepath = "/content/data.txt"  # Replace with the actual file path
word_to_count = "append"  # The word to count
occurrences = count_word_occurrences(filepath, word_to_count)

if isinstance(occurrences, str):  # Check for error message
    print(occurrences)
else:
    print(f"The word '{word_to_count}' appears {occurrences} times in the file.")

"""remove a word from a file"""

# prompt: remove a word from a file

def remove_word_from_file(filepath, word_to_remove):
    """Removes all occurrences of a specific word from a file."""
    try:
        with open(filepath, 'r') as file:
            content = file.read()

        new_content = content.replace(word_to_remove, "")

        with open(filepath, 'w') as file:
            file.write(new_content)
        print(f"All occurrences of '{word_to_remove}' removed from '{filepath}'.")

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")


# Example usage:
filepath = "/content/data.txt"  # Replace with the actual file path
word_to_remove = "append"  # The word to remove
remove_word_from_file(filepath, word_to_remove)

"""file encryption"""

# prompt: encript the contents of data.txt by shifting each character by 2 positions

def encrypt_file(filepath, shift):
    """Encrypts a file by shifting each character by a specified amount."""
    try:
        with open(filepath, 'r') as file:
            content = file.read()

        encrypted_content = ""
        for char in content:
            if 'a' <= char <= 'z':
                encrypted_content += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            elif 'A' <= char <= 'Z':
                encrypted_content += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                encrypted_content += char  # Keep non-alphabetic characters unchanged

        with open(filepath, 'w') as file:
            file.write(encrypted_content)
        print(f"File '{filepath}' encrypted successfully.")

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")

# Example usage
filepath = "/content/data.txt"  # Replace with the actual file path
shift_value = 2  # The amount to shift each character
encrypt_file(filepath, shift_value)

"""file decryption"""

# prompt: decrypt the file encrypted.txt to receive the original content

def decrypt_file(filepath, shift):
    """Decrypts a file that was encrypted using a Caesar cipher."""
    try:
        with open(filepath, 'r') as file:
            content = file.read()

        decrypted_content = ""
        for char in content:
            if 'a' <= char <= 'z':
                decrypted_content += chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            elif 'A' <= char <= 'Z':
                decrypted_content += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                decrypted_content += char

        with open(filepath, 'w') as file:
            file.write(decrypted_content)
        print(f"File '{filepath}' decrypted successfully.")

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")

# Example usage:
filepath = "/content/data.txt"  # Replace with the actual file path
shift_value = 2  # The amount to shift each character (same as used for encryption)
decrypt_file(filepath, shift_value)

"""remove blank lines"""

# prompt: remove blank spaces

import re

def remove_blank_lines(filepath):
    """Removes blank lines from a file."""
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()

        # Use a regular expression to remove lines consisting only of whitespace
        new_content = ''.join(line for line in lines if not re.match(r'^\s*$', line))


        with open(filepath, 'w') as file:
            file.write(new_content)
        print(f"Blank lines removed from '{filepath}'.")

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")


# Example usage:
filepath = "/content/data.txt"  # Replace with the actual file path
remove_blank_lines(filepath)

"""find longest word in a file"""

# prompt: find longest word in a file

import re

def find_longest_word(filepath):
    """Finds the longest word in a file."""
    try:
        with open(filepath, 'r') as file:
            content = file.read()

        # Use a regular expression to find all words (sequences of letters)
        words = re.findall(r'\b[a-zA-Z]+\b', content)

        if not words:
            return "No words found in the file."

        longest_word = max(words, key=len)
        return longest_word

    except FileNotFoundError:
        return f"Error: File '{filepath}' not found."

# Example usage:
filepath = "/content/data.txt"  # Replace with the actual file path
longest_word = find_longest_word(filepath)
print(f"The longest word in the file is: {longest_word}")

"""word frequency analysis"""

# prompt: word frequency analysis

from collections import Counter

def word_frequency(filepath):
    """Performs word frequency analysis on a file."""
    try:
        with open(filepath, 'r') as file:
            content = file.read()

        words = re.findall(r'\b\w+\b', content.lower())  # Find all words, convert to lowercase
        word_counts = Counter(words)
        return word_counts

    except FileNotFoundError:
        return f"Error: File '{filepath}' not found."

# Example usage:
filepath = "/content/data.txt"  # Replace with the actual file path
frequencies = word_frequency(filepath)

if isinstance(frequencies, str):  # Check for error message
    print(frequencies)
else:
    print("Word Frequencies:")
    for word, count in frequencies.most_common():  # Print in descending order of frequency
        print(f"{word}: {count}")