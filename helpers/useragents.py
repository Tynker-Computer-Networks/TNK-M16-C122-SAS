# Importing random
import random
import string


def generateQueryString(length):
    alphanumeric_chars = string.ascii_letters + string.digits
    return ''.join(random.choice(alphanumeric_chars) for _ in range(length))
