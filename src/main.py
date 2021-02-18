import random


def password_generator():
    # generating random letters, digits and signs
    randomUpperCaseLetters = chr(random.randint(65, 90)) + chr(random.randint(65, 90))
    randomLowerCaseLetters = chr(random.randint(97, 122)) + chr(random.randint(97, 122))
    randomDigits = str(random.randint(0,9)) + str(random.randint(0,9))
    randomSign = chr(random.randint(33, 41)) + chr(random.randint(33, 41))

    # putting them al together in a string
    password = randomUpperCaseLetters + randomLowerCaseLetters + randomDigits + randomSign

    # shuffling the string
    password = list (password)
    random.shuffle(password)
    password = ''.join(password)

    return password


