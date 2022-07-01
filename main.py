from encryption import tableDictEncryption
from decryption import tableDictDecryption
import os.path


def encryption():
    while True:
        file = input("Enter the name of the file you would like to encrypt: ")
        file_exists = os.path.exists(file)

        if file_exists:
            while True:
                key = input("Enter the encryption key (numerical): ")
                if key.isnumeric():
                    break
                else:
                    print("You did not enter a valid key!\n")

            with open(file, "r") as text_file:
                text = text_file.read().replace('\n', '')
                break
        else:
            print("File does not exist!\n")

    # Run cipherText algo and append it to file
    cipherText = tableDictEncryption(key, text)
    f = open("cipher.txt", "w")
    f.write(cipherText)
    f.close()

    print("Output generated in ./cipher.txt :)\n")


def decryption():
    print("\nPlease specify the name of the cipher file")
    while True:
        file = input("Enter the name of the cipher file: ")
        file_exists = os.path.exists(file)

        if file_exists:
            while True:
                key = input("Enter the encryption key (numerical): ")
                if key.isnumeric():
                    break
                else:
                    print("You did not enter a valid key!\n")
            break  # All checks passed, proceed to decrypt
        else:
            print("You did not specify a vaid cipher file!\n")

    # Read cipher file
    with open(file, "r") as text_file:
        cipherText = text_file.readlines()

    cipherText = cipherText[0]
    print(tableDictDecryption(key, cipherText))  # print to cli


def main():
    print("1. Encryption")
    print("2. Decryption")

    while True:
        mode = input("Choose your mode(1,2): ")
        if mode == '1':
            encryption()
        elif mode == '2':
            try:
                decryption()
            except:
                # If there is an error then they have not passed in the same key
                # that they initially encrypted the file with
                print("You must decrypt using the correct key!!\n")
        else:
            print("\nYou have entered an incorrect input!")


if __name__ == "__main__":
    main()
