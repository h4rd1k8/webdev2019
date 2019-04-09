a = int(input())
for number in range(2, a + 1):
    if a % number == 0:
        print(number)
        break
