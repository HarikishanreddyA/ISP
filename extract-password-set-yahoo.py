# Initialize an empty list to store passwords
passwords = []

# Flag to indicate when to start extracting lines
extracting = False

# Read the file and process it line by line
with open('password.file', 'r', encoding='latin-1') as file:
    for line in file:
        # Check if the line contains "email:pass dump" to indicate the start of the relevant section
        if "email:pass dump" in line:
            extracting = True
        elif extracting and ":" in line:
            parts = line.strip().split(':')
            if len(parts) == 3:
                _, _, password = parts  # We don't need the username, so skip it
                passwords.append(password)

# Write the extracted passwords to a new file called 'given-set.txt'
with open('given-set.txt', 'w') as output_file:
    for password in passwords:
        output_file.write(password + '\n')
