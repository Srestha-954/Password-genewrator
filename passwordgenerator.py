import random
import string

def generate_password(length, complexity):
    if complexity == "easy":
        characters = string.ascii_letters
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    else:  # strong
        characters = string.ascii_letters + string.digits + string.punctuation

    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
try:
    length = int(input("Enter the desired password length: "))
    if length < 4:
        print("Password length should be at least 4 for better security.")
    else:
        complexity = input("Choose complexity (easy / medium / strong): ").lower()
        if complexity not in ["easy", "medium", "strong"]:
            print("Invalid choice. Defaulting to 'strong'.")
            complexity = "strong"

        count = int(input("How many passwords do you want to generate? "))

        print("\nGenerated Passwords:")
        for i in range(count):
            password = generate_password(length, complexity)
            print(f"{i+1}: {password}")

except ValueError:
    print("Please enter a valid number.")
