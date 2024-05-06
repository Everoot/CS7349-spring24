import zipfile

def dictionary_attack(zip_file_name, dictionary_file):
    # Attempt to open the dictionary file and read passwords
    try:
        with open(dictionary_file, 'r') as dict_file:
            passwords = dict_file.read().splitlines()
    except FileNotFoundError:
        print("Dictionary file not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the dictionary file: {e}")
        return

    # Initialize the ZipFile object
    try:
        with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
            for password in passwords:
                try:
                    # Attempt to extract the zip file with the current password
                    zip_ref.extractall(pwd=bytes(password, 'utf-8'))
                    print(f"Success! File extracted with password: {password}")
                    return
                except RuntimeError as e:
                    # Handling incorrect password exception
                    continue
                except zipfile.BadZipFile:
                    print("File is not a zip file or the zip file is corrupted.")
                    return
    except FileNotFoundError:
        print("Zip file not found.")
    except Exception as e:
        print(f"An error occurred while processing the zip file: {e}")

# Specify the filename of the password-protected zip file
zip_file_name = 'HW3_evil.zip'
# Specify the dictionary file containing potential passwords
dictionary_file = 'HW3dictionary.txt'

# Call the function to perform a dictionary attack on the zip file
dictionary_attack(zip_file_name, dictionary_file)
