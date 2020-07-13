# Scott Hudson
# CS 362 HW3: Random Testing Hands On

import unittest
import random

from credit_card_validator import credit_card_validator


class CreditCardTests(unittest.TestCase):

    number_of_tests = 10000

    # Visa Tests

    # Visa prefix, more than 16 digits, check sum is random
    for i in range(number_of_tests):
        num = random.randint(40000000000000000, 49999999999999999)
        credit_card_validator(str(num))

    # Visa prefix, 16 digits, check sum is random
    for i in range(number_of_tests):
        num = random.randint(4000000000000000, 4999999999999999)
        credit_card_validator(str(num))

    # Visa prefix, less than 16 digits, check sum is random
    for i in range(number_of_tests):
        num = random.randint(400000000000000, 499999999999999)
        credit_card_validator(str(num))

    # Visa prefix, less than 16 digits, check sum is random
    for i in range(number_of_tests):
        num = random.randint(400000000000000, 499999999999999)
        credit_card_validator(str(num))

    # Master Card tests

    # Mastercard random prefix between 51 and 55 (allows for outliers)
    # less than 16 digits, check sum is random
    for i in range(number_of_tests):
        num = random.randint(500000000000000, 569999999999999)
        credit_card_validator(str(num))

    # Mastercard random prefix between 2221 and 2720 (allows for outliers)
    # less than 16 digits, check sum is random
    for i in range(number_of_tests):
        num = random.randint(400000000000000, 499999999999999)
        credit_card_validator(str(num))

    # Mastercard random prefix between 51 and 55 (allows for outliers)
    # 16 digits, check sum is random
    for i in range(number_of_tests):
        num = random.randint(5000000000000000, 5699999999999999)
        credit_card_validator(str(num))

    # Mastercard random prefix between 2221 and 2720 (allows for outliers)
    # 16 digits, check sum is random
    for i in range(number_of_tests):
        num = random.randint(4000000000000000, 4999999999999999)
        credit_card_validator(str(num))

    # Mastercard random prefix between 51 and 55 (allows for outliers)
    # more than 16 digits, check sum is random
    for i in range(number_of_tests):
        num = random.randint(500000000000000, 569999999999999)
        credit_card_validator(str(num))

    # Mastercard random prefix between 2221 and 2720 (allows for outliers)
    # more than 16 digits, check sum is random
    for i in range(number_of_tests):
        num = random.randint(40000000000000000, 49999999999999999)
        credit_card_validator(str(num))

    # American Express tests


if __name__ == '__main__':
    unittest.main(verbosity=2)
