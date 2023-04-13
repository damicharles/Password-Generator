import random
import string

# Ask the user for password preferences
length_of_password = int(input("Enter the desired length of your password: "))
complexity_of_password = input("Enter the desired complexity of your password (low, medium, or high): ")

# Define character sets based on complexity level
if complexity_of_password == "low":
    chars = string.ascii_letters
elif complexity_of_password == "medium":
    chars = string.ascii_letters + string.digits
elif complexity_of_password == "high":
    chars = string.ascii_letters + string.digits + string.punctuation

# Generate a random password
password = ""
for i in range(length_of_password):
    password += random.choice(chars)

# Print the generated password
print("Your password is:", password)
