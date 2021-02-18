import random

# the goal of this function is to generate 8 random characters


def password_generator():
    # generating random letters, digits and signs
    random_upper_case_letters = chr(random.randint(65, 90)) + chr(random.randint(65, 90))
    random_lower_case_letters = chr(random.randint(97, 122)) + chr(random.randint(97, 122))
    random_digits = str(random.randint(0,9)) + str(random.randint(0,9))
    random_signs = chr(random.randint(33, 41)) + chr(random.randint(33, 41))

    # putting them al together in a string
    password = random_upper_case_letters + random_lower_case_letters + random_digits + random_signs

    # shuffling the string
    password = list (password)
    random.shuffle(password)
    password = ''.join(password)

    return password


