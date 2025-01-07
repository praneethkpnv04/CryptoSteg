import getpass
import subprocess
import sys

print("""
				|--------------------------|
				|C-r-y-p-t-o-S-t-e-g	   |
				|--------------------------|
""")
def ccrypt_encrypt(filename):
    subprocess.run(["ccrypt", "-e", filename])

def ccrypt_decrypt(filename):
    subprocess.run(["ccrypt", "-d", filename])

def steghide_hide(file_to_hide, image_file, password):
    subprocess.run(["steghide", "embed", "-cf", image_file,"-ef",file_to_hide,"-p", password])

def steghide_extract(image_file,password):            
    subprocess.run(["steghide", "extract", "-sf", image_file, "-p", password])

def crypto_steg(file_to_hide, image_file, password):
    #ccrypt_encrypt(file_to_hide)
    steghide_hide(file_to_hide , image_file, password)

def crypto_steg_decrypt(image_file, password):
    #steghide_extract(image_file, output_file + ".ccrypt", password)
     steghide_extract(image_file, password)
    #ccrypt_decrypt(output_file + ".ccrypt")

def main():
    while True:
        print("Menu:")
        print("1. ccrypt")
        print("2. steghide")
        print("3. CryptoSteg")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice in ("1", "2", "3", "4"):
            if choice == "1":
                while True:
                    print("\n1. Encrypt")
                    print("2. Decrypt")
                    print("3. Back")
                    choice1 = input("Enter your choice: ")
                    if choice1 in ("1", "2", "3"):
                        if choice1 == "1":
                            filename = input("Enter the file to encrypt: ")
                            ccrypt_encrypt(filename)
                        elif choice1 == "2":
                            filename = input("Enter the file to decrypt: ")
                            ccrypt_decrypt(filename)
                        elif choice1 == "3":
                            break  # Go back to main menu
                    else:
                        print("Invalid choice. Please try again.")

            elif choice == "2":
                while True:
                    print("\n1. Hide")
                    print("2. Extract")
                    print("3. Back")
                    choice2 = input("Enter your choice: ")
                    if choice2 in ("1", "2", "3"):
                        if choice2 == "1":
                            file_to_hide = input("Enter the file to hide: ")
                            image_file = input("Enter the image file: ")
                            password = getpass.getpass("Enter the password: ")
                            steghide_hide(file_to_hide, image_file, password)
                        elif choice2 == "2":
                            image_file = input("Enter the image file: ")
                            password = getpass.getpass("Enter the password: ")
                            steghide_extract(image_file, "output_file", password)  # Assume output_file as fixed name
                        elif choice2 == "3":
                            break  # Go back to main menu

            elif choice == "3":
                while True:
                    print("\n1. Encrypt")
                    print("2. Hide")
                    print("3. Extract")
                    print("4. Decrypt")
                    print("5. Back")
                    choice3 = input("Enter your choice: ")
                    if choice3 in ("1", "2", "3", "4", "5"):
                        if choice3 == "1":
                            filename = input("Enter the file to encrypt: ")
                            ccrypt_encrypt(filename)
                        elif choice3 == "2":
                            file_to_hide = input("Enter the file to hide: ")
                            image_file = input("Enter the image file: ")
                            password = getpass.getpass("Enter the password: ")
                            crypto_steg(file_to_hide, image_file, password)
                        elif choice3 == "3":
                            image_file = input("Enter the image file: ")
                            #output_file = input("Enter the output file name: ")
                            password = getpass.getpass("Enter the password: ")
                            crypto_steg_decrypt(image_file, password)
                        elif choice3 == "4":
                            filename = input("Enter the encrypted file to decrypt: ")
                            ccrypt_decrypt(filename)
                        elif choice3 == "5":
                            break  # Go back to main menu
                    else:
                        print("Invalid choice. Please try again.")

            elif choice == "4":
                print("EXITING...")
                sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
