n = int(input())
line = input().split(' ')
for i in range(len(line) - 1, -1, -1):
    print(int(line[i]), end = " ")