n = int(input())
a = []
line = input().split(" ")
for i in range(0, len(line)):
    a.append(int(line[i]))
same_signed = False
for i in range(1, n):
    if a[i - 1] * a[i] >+ 0:
        same_signed = True
        break
if same_signed:
    print("YES")
else:
    print("NO")
