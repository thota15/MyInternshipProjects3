import string
import secrets

def generate_password(length=12):
    # Define character sets for password components
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Create a pool of characters to generate the password
    all_chars = uppercase_chars + lowercase_chars + digits + special_chars

    # Ensure that at least one character from each category is included
    password = [
        secrets.choice(uppercase_chars),
        secrets.choice(lowercase_chars),
        secrets.choice(digits),
        secrets.choice(special_chars)
    ]

    # Fill the rest of the password length randomly
    remaining_length = length - len(password)
    password.extend(secrets.choice(all_chars) for _ in range(remaining_length))

    # Shuffle the characters to make the password more secure
    secrets.SystemRandom().shuffle(password)

    # Convert the list of characters to a string
    return ''.join(password)

def main():
    try:
        password_length = int(input("Enter the desired password length: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))
        
        for _ in range(num_passwords):
            password = generate_password(password_length)
            print(password)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
