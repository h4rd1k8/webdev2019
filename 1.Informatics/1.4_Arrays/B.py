n = int(input())
a = []
numbers = input().split(' ')
for i in range(0, n):
    a.append(int(numbers[i]))
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        print(a[i], end = " ")
