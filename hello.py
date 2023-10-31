def password_encoder(encoder_string):
    password_format = list(encoder_string)
    new_list = []
    for n in range(0, len(password_format)):
        password_addition = (int(password_format[n]) + 3) % 10
        new_list.append(str(password_addition))

    string_password = ''.join(new_list)


    return(string_password)


def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    while True:
        user_input = input("Please enter an option: ")
        if user_input == 1:
            option = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")

        if user_input == 2:
            print(f"The encoded password is {password_encoder(option)}, and the original password is {option}.")

        if user_input == 3:
            break

if __name__ =="__main__":
    menu()




