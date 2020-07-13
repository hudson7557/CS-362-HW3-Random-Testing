# Scott Hudson
# CS 362 HW3: Random Testing Hands On

import unittest
import random
from credit_card_validator import credit_card_validator


class CreditCardTests(unittest.TestCase):

    def visa_17_digits(self):
        number_of_tests = 10000
        for i in range(number_of_tests):
            num = random.randint(40000000000000000, 49999999999999999)
            credit_card_validator(num)

    def visa_16_digits(self):
        number_of_tests = 10000
        for i in range(number_of_tests):
            num = random.randint(4000000000000000, 4999999999999999)
            credit_card_validator(num)

    def visa_15_digits(self):
        number_of_tests = 10000
        for i in range(number_of_tests):
            num = random.randint(400000000000000, 499999999999999)
            credit_card_validator(num)


# Master Card generators

# American Express generator


if __name__ == '__main__':
    unittest.main(verbosity=2)
