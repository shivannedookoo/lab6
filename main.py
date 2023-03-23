# Shivanne Dookoo

def encode(password):  # shifts each digit of an 8-digit password by 3 numbers
    encoded_password = ""
    for digit in password:
        if (int(digit) + 3) >= 10:
            encoded = str((int(digit) + 3) % 10) # shifts each digit up by 3 and keeps remainder for values more than 10
        else:
            encoded = str((int(digit) + 3)) # ensures we are not taking the remainder of values less then 10
        encoded_password += encoded
    return encoded_password


def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded = str((int(digit) - 3) % 10)  # shifts each digit down by 3 and keeps remainder for values more than 10
        decoded_password += decoded
    return decoded_password


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
            print(f"The encoded password is {encode}, and the original password is {decode(encode)}.\n" )
        if option == 3:  # quits
            break

