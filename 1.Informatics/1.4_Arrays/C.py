n = int(input())
a = []
cnt = 0
numbers = input().split(' ')
for i in range(0, n):
    a.append(int(numbers[i]))
for i in range(0, len(a)):
    if a[i] > 0:
        cnt += 1
print(cnt)