n = int(input())
a = []
numbers = input().split(' ')
for i in range(0, n):
    a.append(int(numbers[i]))
for i in range(0, len(a), 2):
    print(a[i], end = " ")
