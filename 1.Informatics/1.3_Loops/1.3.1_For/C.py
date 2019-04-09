import math
for number in range(int(input()), int(input()) + 1, 1):
    if int(math.sqrt(number)) ** 2 == int(number):
        print(number, end = " ")