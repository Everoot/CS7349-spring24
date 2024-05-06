# Import the crypt library for hashing functions
import crypt

# Define a function to attempt cracking a single encrypted password
def attempt_password_crack(encrypted_password):
    # Extract the first two characters of the encrypted password as the salt
    salt = encrypted_password[:2]
    # Open the dictionary file
    with open('HW3dictionary.txt', 'r') as dictionary_file:
        # Iterate over each word in the dictionary file
        for word in dictionary_file:
            # Remove the newline character at the end of each word
            word = word.strip('\n')
            # Encrypt the word from the dictionary using the extracted salt
            encrypted_word = crypt.crypt(word, salt)
            # If the encrypted word matches the user's encrypted password
            if (encrypted_word == encrypted_password):
                # Password found, print the result and return
                print("[+] Found Password: " + word)
                return True
    # If no password is found after going through the dictionary
    print("[-] Password Not Found.")
    return False

# Define the main function
def main():
    # Open the password file
    with open('HW3passwords.txt') as password_file:
        # Iterate over each line in the password file
        for line in password_file:
            if ":" in line:
                # Extract the username and the encrypted password
                user = line.split(':')[0]
                encrypted_password = line.split(':')[1].strip()
                # Print which user's password is currently being attempted
                print("[*] Cracking Password For: " + user)
                # Call the function to attempt cracking the password
                attempt_password_crack(encrypted_password)

# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()
