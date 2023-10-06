import re


def check_email(email: str):
    pattern = (
        # Prefix
        "[A-Za-z0-9]+([\._-][A-Za-z0-9]+)*"
        # @ Character
        "@"
        # Suffix
        "[A-Za-z0-9-]+[.][A-Za-z0-9-]{2,}"
    )
    found = re.fullmatch(pattern, email)
    return bool(found)


def check_password(password: str):
    safe = False

    pattern = (
        # Start of string
        "^"
        # At least one number
        "(?=.*[0-9]+.*)"
        # At least one lowercase letter
        "(?=.*[a-z]+.*)"
        # At least one uppercase letter
        "(?=.*[A-Z]+.*)"
        # At least one special character
        "(?=.*[!@#$%&_=,/<>?;':^*()+.\"{}\[\]\\\\-]+.*)"
        # No whitespace characters
        "(?!.*\s+.*)"
        # At least 8 characters
        ".{8,}"
        # End of string
        "$"
    )

    password_check = re.match(pattern, password)
    if password_check:
        safe = True

    return safe


if __name__ == '__main__':
    valid = False
    print("Provide an e-mail: ")
    while not valid:
        email = input()

        valid = check_email(email)
        if valid:
            print(u'\u2713' + " E-mail is valid")
        else:
            print("x E-mail is not valid")
            print("\nProvide an e-mail: ")

    secure = False
    while not secure:
        print('\nProvide a secure password: ')
        password = input()
        secure = check_password(password)
        if secure:
            print(u'\u2713' + ' Password meets the security requirements')

        else:
            print("x Password does not meet requirements")
            print("- At least one uppercase letter")
            print("- At least one lowercase letter")
            print("- At least one digit")
            print("- At least one special character")
            print("- At least 8 characters")
            print("- No whitespace characters")
