# Shivanne Dookoo

def encode(password):  # shifts each digit of an 8-digit password by 3 numbers
    encoded_password = ""
    for digit in password:
        encoded = str((int(digit) + 3) % 10)  # shifts each digit up by 3 and keeps remainder for values more than 10
        encoded_password += encoded
    return encoded_password





if __name__ == "__main__":
    while True:
        print("Menu")  # prints menu
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        option = int(input("Please enter an option: "))  # prompts user to choose a menu option

        if option == 1:  # encodes password
            password = str(input("Please enter your password to encode: "))  # prompts user to input an 8-digit password
            encode = encode(password)
            print("Your password has been encoded and stored!\n")
        if option == 2:
            pass
        if option == 3:  # quits
            break

