import re


def check_email_prefix(email_prefix: str):
    found = re.fullmatch("[A-Za-z0-9]+([\._-][A-Za-z0-9]+)*", email_prefix)
    return bool(found)


def check_email_suffix(email_suffix: str):
    found = re.fullmatch("[A-Za-z0-9-]+[.][A-Za-z0-9-]{2,}", email_suffix)
    print(found)
    return bool(found)


if __name__ == '__main__':
    print("Provide an e-mail: ")
    email = input()

    split_email = email.split("@")
    if len(split_email) != 2:
        print(f"E-mail {email} is not valid")
        exit(1)

    email_prefix, email_suffix = email.split("@")

    if check_email_prefix(email_prefix) and check_email_suffix(email_suffix):
        print("E-mail is valid")
    else:
        print("E-mail is not valid")
