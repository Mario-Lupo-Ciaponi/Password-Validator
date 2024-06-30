import string


def requirements():
    print("1) Password must contain at least 16 characters;\n"
          "2) Password must contain at least one digit;\n"
          "3) Password must contain at least one uppercase letter;\n"
          "4) Password must contain at least one lowercase letter;\n"
          "5) Password must contain at least one special symbol.\n")


def is_password_long_enough(password):
    if len(password) >= 16:
        return True

    return False


def is_there_digit(all_symbols_in_the_password):
    for symbol in all_symbols_in_the_password:
        if symbol.isdigit():
            return True

    return False


def is_there_a_uppercase_letter(all_symbols_in_the_password):
    for symbol in all_symbols_in_the_password:
        if symbol.isupper():
            return True

    return False


def is_there_a_lowercase_letter(all_symbols_in_the_password):
    for symbol in all_symbols_in_the_password:
        if symbol.islower():
            return True

    return False


def is_there_a_special_symbol(all_symbols_in_the_password):
    for symbol in all_symbols_in_the_password:
        if symbol in string.punctuation:
            return True

    return False


def is_password_valid(password):
    print()

    all_symbols_in_the_password = set(password)

    if not is_password_long_enough(password):
        print("Password length must be at least 16 characters long!")
    if not is_there_digit(all_symbols_in_the_password):
        print("Password must contain at least one digit!")
    if not is_there_a_uppercase_letter(all_symbols_in_the_password):
        print("Password must contain at least one uppercase letter!")
    if not is_there_a_lowercase_letter(all_symbols_in_the_password):
        print("Password must contain at least one lowercase letter!")
    if not is_there_a_special_symbol(all_symbols_in_the_password):
        print("Password must contain at least one special symbol!")

    is_valid = (is_password_long_enough(password) and is_there_digit(password) and
                is_there_a_uppercase_letter(password) and is_there_a_lowercase_letter(password) and
                is_there_a_special_symbol(password))

    if is_valid:
        return True
    else:
        return False


def main():
    while True:
        requirements()
        password = input("Password:")

        is_valid = is_password_valid(password)

        if is_valid:
            print("Password is valid")
            break

        print()  # For look prettier in the console


if __name__ == "__main__":
    main()
