import hashlib
import os


# Function to generate a random salt
def generate_salt():
    return os.urandom(16)

# Function to hash a password with a salt using SHA-256
def hash_password(password, salt):
    salted_password = password.encode('utf-8') + salt
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return hashed_password


# Function to read hashed passwords from a file
def read_hashed_passwords(filename):
    with open(filename, 'r') as file:
        return {line.strip() for line in file}


if __name__ == "__main__":
    # Read the known hashes from the formspring.txt file
    known_hashes = read_hashed_passwords("formspring.txt")

    # Input file containing passwords to test
    input_filename = "password-test.txt"

    # Process passwords from the input file
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            password = line.strip()
            salt = generate_salt()
            hashed_password = hash_password(password, salt)
            if hashed_password in known_hashes:
                print(f"Password '{password}' matches a known hash.")
