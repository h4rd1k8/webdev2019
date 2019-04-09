n = int(input())
i = 1
is_pow = False
while i <= n:
    if i == n:
        print("YES")
        is_pow = True
        break;
    i *= 2
if not is_pow:
    print("NO")