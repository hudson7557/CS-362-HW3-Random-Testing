import math
nums = [4052598627176748,
        4052394246435131,
        4052394246435131,
        4052297815102877,
        4052261085590328,
        4052187300995200,
        4052827547288782,
        4052903423124761,
        4052958378874711,
        4052977245094154]

for num in nums:
    print(round(num, -16))
    if round(num, -15) > 4000000000000000:
        print(round(num, -15), "okay")

num = "4089767900471111"
total = 0

for digit in num:
    total = total + int(digit)

print(total)