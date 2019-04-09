n = int(input())
line = input().split(' ')
cnt = 0
a = []
for i in range(0, len(line)):
    a.append(int(line[i]))
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] and a[i + 1] < a[i]:
        cnt += 1
print(cnt)