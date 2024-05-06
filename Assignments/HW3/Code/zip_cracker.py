import zipfile

def extract_zip(zip_file_name, password):
    # try:
    #     # Instantiate a ZipFile object
    #     with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
    #         # Use the extractall method and provide the password
    #         zip_ref.extractall(pwd=bytes(password, 'utf-8'))
    #         print("Extraction successful. Contents extracted.")
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    try:
        # Instantiate a ZipFile object
        with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
            # Use the extractall method and provide the password
            zip_ref.extractall(pwd=bytes(password, 'utf-8'))
            print("Extraction successful. Contents extracted.")
    except RuntimeError as e:
        # Catching exceptions related to incorrect password
        if 'Bad password' in str(e):
            print("Incorrect password provided.")
        else:
            print(f"Runtime error occurred: {e}")
    except zipfile.BadZipFile:
        print("File is not a zip file or the zip file is corrupted.")
    except Exception as e:
        # Catching other general exceptions
        print(f"An error occurred: {e}")


# Specify the filename of the password-protected zip file
zip_file_name = 'HW3_evil.zip'
# Specify an incorrect password
password = 'wrong_password'

# Call the function to extract the zip file
extract_zip(zip_file_name, password)
