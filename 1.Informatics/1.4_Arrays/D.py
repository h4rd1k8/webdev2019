n = int(input())
line = input().split(' ')
i = 1
cnt = 0
for i in range(1, len(line)):
    if int(line[i]) > int(line[i-1]):
        cnt += 1
print(cnt)