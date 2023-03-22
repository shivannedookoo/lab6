# Shivanne Dookoo

def encode(password):
    encoded_password = ""
    for digit in password:
        encoded = str((int(digit) + 3) % 10)
        encoded_password += encoded
    return encoded_password





if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        option = int(input("Please enter an option: "))

        if option == 1:
            password = str(input("Please enter your password to encode: "))
            encode = encode(password)
            print("Your password has been encoded and stored!\n")
        if option == 2:
            pass
        if option == 3:
            break

