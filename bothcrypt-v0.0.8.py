from cryptography.fernet import Fernet

while True:
    start = input("> ")
    if start == "start":
        encryptChoice = input("Would you like to encrypt or decrypt a file? (E/D)")
        encryptChoice = encryptChoice.upper()
        if encryptChoice == "E":
            fileName = input("Enter the name of the file you want to encrypt: ")
            # key generation
            key = Fernet.generate_key()

            # string the key in a file
            with open(f'{fileName}.key', 'wb') as filekey:
                filekey.write(key)

            # opening the key
            with open(f'{fileName}.key', 'rb') as filekey:
                key = filekey.read()

            # using the generated key
            fernet = Fernet(key)

            # opening the original file to encrypt
            with open(f'{fileName}', 'rb') as file:
                original = file.read()
                
            # encrypting the file
            encrypted = fernet.encrypt(original)

            # opening the file in write mode and
            # writing the encrypted data
            with open(f'{fileName}', 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
        elif encryptChoice == "D":
            fileName = input("Enter the name of the file you want to decrypt: ")
            with open(f'{fileName}.key', 'rb') as decry:
                key = decry.read()

                # using the key
                fernet = Fernet(key)

                # opening the encrypted file
                with open(f'{fileName}', 'rb') as enc_file:
                    encrypted = enc_file.read()

                decrypted = fernet.decrypt(encrypted)

                # opening the file in write mode and
                # writing the decrypted data
                with open(f'{fileName}', 'wb') as dec_file:
                    dec_file.write(decrypted)
    elif start == "exit":
        exit()
    else:
        print("Unknown Command. ")