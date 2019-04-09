def mini(a, b):
    if a < b:
        return a
    else:
        return b


def mini4(a, b, c, d):
    return mini(mini(a, b), mini(c, d))


line = input().split(' ')
print(mini4(int(line[0]), int(line[1]), int(line[2]), int(line[3])))



