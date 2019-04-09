def power(a, b):
    po = a
    if b == 0:
        return 1
    else:
        for i in range(1, b):
            po *= a
        return po


line = input().split()
print(power(float(line[0]), int(line[1])))
