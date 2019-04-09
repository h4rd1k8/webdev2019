a = int(input())
cnt = 0
for i in range(1, int(a ** 0.5) + 1):
    if a % i == 0:
        cnt += 1

if a ** 0.5 == int(a ** 0.5):
    print(cnt * 2 - 1)
else:
    print(cnt * 2)