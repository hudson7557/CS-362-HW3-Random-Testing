import random


def visa_17_digits():
    number_of_tests = 10000
    for i in range(number_of_tests):
        num = random.randint(40000000000000000, 49999999999999999)
        print(str(num))
