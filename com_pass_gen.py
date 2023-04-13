import random
import string

# Define the character sets
uppercase_chars = string.ascii_uppercase
lowercase_chars = string.ascii_lowercase
digit_chars = string.digits
symbol_chars = string.punctuation

# Ask the user for password preferences
length = int(input("Enter the desired length of your password: "))
uppercase = input("Include uppercase letters? (y/n): ")
lowercase = input("Include lowercase letters? (y/n): ")
digits = input("Include digits? (y/n): ")
symbols = input("Include symbols? (y/n): ")

# Generate the character set based on user preferences
chars = ""
if uppercase.lower() == "y":
    chars += uppercase_chars
if lowercase.lower() == "y":
    chars += lowercase_chars
if digits.lower() == "y":
    chars += digit_chars
if symbols.lower() == "y":
    chars += symbol_chars

# Check if at least one character set is included
if chars == "":
    print("Error: You must include at least one character set.")
    exit()

# Generate a random password
password = ""
for i in range(length):
    password += random.choice(chars)

# Print the generated password
print("Your password is:", password)
