from src.main import password_generator


upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
signs = "!@#$%^&*()"


# main test function
def test_password_generator():
    password = password_generator()
    assert length_check(password), "is the password contain 8 characters"
    assert upper_case_check(password), "is the password have 2 upper case letters"
    assert lower_case_check(password), "is the password have 2 lower case letters"
    assert signs_check(password), "is the password contain 2 signs"


# functions within the main function


def length_check(password):
    if len(password) == 8:
        return True
    else:
        return False


def upper_case_check(password):
    cnt = 0
    for i in range(len(upper_case_letters)):
        if upper_case_letters[i] in password:
            password = list(password)
            password.remove(upper_case_letters[i])
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False


def lower_case_check(password):
    cnt = 0
    for i in range(len(lower_case_letters)):
        if lower_case_letters[i] in password:
            password = list(password)
            password.remove(lower_case_letters[i])
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False


def signs_check(password):
    cnt = 0
    for i in range(len(signs)):
        if signs[i] in password:
            password = list(password)
            password.remove(signs[i])
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False






