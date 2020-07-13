# Scott Hudson
# CS 362 HW3: Random Testing Hands On

import unittest
import random

from credit_card_validator import credit_card_validator


class CreditCardTests(unittest.TestCase):

    number_of_tests = 10000

    # Visa Tests

    # Visa prefix, less than 16 digits, check sum is random
    for i in range(number_of_tests):
        num = random.randint(390000000000000, 590000000000000)
        credit_card_validator(str(num))

    # Visa prefix, 16 digits, check sum is random
    for i in range(number_of_tests):
        num = random.randint(3900000000000000, 5900000000000000)
        credit_card_validator(str(num))

    # Visa prefix, more than 16 digits, check sum is random
    for i in range(number_of_tests):
        num = random.randint(39000000000000000, 59000000000000000)
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
        num = random.randint(222000000000000, 272999999999999)
        credit_card_validator(str(num))

    # Mastercard random prefix between 51 and 55 (allows for outliers)
    # 16 digits, check sum is random
    for i in range(number_of_tests):
        num = random.randint(5000000000000000, 5699999999999999)
        credit_card_validator(str(num))

    # Mastercard random prefix between 2221 and 2720 (allows for outliers)
    # 16 digits, check sum is random
    for i in range(number_of_tests):
        num = random.randint(2220000000000000, 2729999999999999)
        credit_card_validator(str(num))

    # Mastercard random prefix between 51 and 55 (allows for outliers)
    # more than 16 digits, check sum is random
    for i in range(number_of_tests):
        num = random.randint(50000000000000000, 56999999999999999)
        credit_card_validator(str(num))

    # Mastercard random prefix between 2221 and 2720 (allows for outliers)
    # more than 16 digits, check sum is random
    for i in range(number_of_tests):
        num = random.randint(22200000000000000, 27299999999999999)
        credit_card_validator(str(num))

    # American Express tests



if __name__ == '__main__':
    unittest.main(verbosity=2)
