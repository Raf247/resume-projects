from cryptography.fernet import Fernet
import os

#Function to generate a key and save it into a file
def generate_key():
    key = Fernet.generate_key() #Generate a new key
    with open("Secret.key", "wb") as key_file: #Open the key file in write-binary mode
        key_file.write(key) #Write the generated key to the file

#Function to load key from previous saved file
def load_key():
    return open("Secret.key", "rb").read() # Open the key file in read-binary mode and return contents

#Function to encrypt a file using a provided key
def encrypt(filename, key):
    f = Fernet(key) #Create a fernet object with given key
    with open(filename, "rb")as file:  #Open target file in read-binary mode
        file_data = file.read() #Read file data
        enccrypted_data = f.encrypt(file_data) #Encrypt data
    with open(filename, "wb") as file: #Open the target file in write-binary mode
        file.write(enccrypted_data) #Write the encrypted data back to the file

#Function to decrypt a file using a provided key
def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file: #Open encrypted file in read-binary mode
        encrypted_data = file.read() #Read encrypted data
        try:
            decrypted_data = f.decrypt(encrypted_data)
        except InvalidToken: #Handle the exception if the key is invalid
            print("Invalid Key")
            return
    with open(filename, "wb") as file:
        file.write(decrypted_data) #Write decrypted data back to the file

choice = input("Enter 'e' to encrypt or 'd' to decrypt the file.").lower()
if choice == 'e':
    filename = input("Enter the file name to encrypt(including file extension): ")
    if os.path.exists(filename): #Check if the file exists
        generate_key() #Generate and save new key
        key = load_key() #Load new saved key
        encrypt(filename, key) #Encrypt file
        print("File encrypted successfully")
    else:
        print(f"file '{filename} not found. Please try again")

elif choice == 'd':
    filename = input("Enter the file name to encrypt(including file extension): ")
    if os.path.exists(filename): #Check if the file exists
        key = load_key() #Load existing key
        decrypt(filename, key) #Decrypt file
        print("File decrypted successfully")
    else:
        print(f"file '{filename} not found. Please try again")

else:
    print("Invalid choice. Please enter 'e' to encrypt file or 'd' to decrypt file")
    