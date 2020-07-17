# Scott Hudson
# CS 362 HW3: Random Testing Hands On

import unittest
import random

from credit_card_validator import credit_card_validator


class CreditCardTests(unittest.TestCase):

    number_of_visa_tests = 60000
    number_of_mc_tests = 60000
    number_of_ae_tests = 120000

    # Visa Tests

    # Visa prefix, less than 16 digits, check sum is random
    for i in range(number_of_visa_tests):
        num = random.randint(390000000000000, 590000000000000)
        credit_card_validator(str(num))

    # Visa prefix, 16 digits, check sum is random
    for i in range(number_of_visa_tests):
        num = random.randint(3900000000000000, 5900000000000000)
        credit_card_validator(str(num))

    # Visa prefix, more than 16 digits, check sum is random
    for i in range(number_of_visa_tests):
        num = random.randint(39000000000000000, 59000000000000000)
        credit_card_validator(str(num))

    # MasterCard tests

    # MasterCard random prefix between 51 and 55 (allows for outliers)
    # less than 16 digits, check sum is random
    for i in range(number_of_mc_tests):
        num = random.randint(500000000000000, 569999999999999)
        credit_card_validator(str(num))

    # MasterCard random prefix between 2221 and 2720 (allows for outliers)
    # less than 16 digits, check sum is random
    for i in range(number_of_mc_tests):
        num = random.randint(222000000000000, 272999999999999)
        credit_card_validator(str(num))

    # MasterCard random prefix between 51 and 55 (allows for outliers)
    # 16 digits, check sum is random
    for i in range(number_of_mc_tests):
        num = random.randint(5000000000000000, 5699999999999999)
        credit_card_validator(str(num))

    # MasterCard random prefix between 2221 and 2720 (allows for outliers)
    # 16 digits, check sum is random
    for i in range(number_of_mc_tests):
        num = random.randint(2220000000000000, 2729999999999999)
        credit_card_validator(str(num))

    # MasterCard random prefix between 51 and 55 (allows for outliers)
    # more than 16 digits, check sum is random
    for i in range(number_of_mc_tests):
        num = random.randint(50000000000000000, 56999999999999999)
        credit_card_validator(str(num))

    # MasterCard random prefix between 2221 and 2720 (allows for outliers)
    # more than 16 digits, check sum is random
    for i in range(number_of_mc_tests):
        num = random.randint(22200000000000000, 27299999999999999)
        credit_card_validator(str(num))

    # American Express tests
    # The two prefixes were combined to allow for outlier testing for prefixes
    # 35 and 36, rather than generate twice just generates in the range and
    # doubles the amount to account for less calls.

    # American Express prefix around 34 and 37 (allows for outliers)
    # less than 15 digits, check sum is random
    for i in range(number_of_ae_tests):
        num = random.randint(32000000000000, 38999999999999)
        credit_card_validator(str(num))

    # American Express prefix around 34 and 37 (allows for outliers)
    # 15 digits, check sum is random
    for i in range(number_of_ae_tests):
        num = random.randint(320000000000000, 389999999999999)
        credit_card_validator(str(num))

    # American Express prefix around 34 and 37 (allows for outliers)
    # more than 15 digits, check sum is random
    for i in range(number_of_ae_tests):
        num = random.randint(3200000000000000, 3899999999999999)
        credit_card_validator(str(num))


if __name__ == '__main__':
    unittest.main(verbosity=2)

