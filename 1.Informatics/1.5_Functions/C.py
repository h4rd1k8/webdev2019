def new_xor(a, b):
    return int(a != b)


if __name__ == "__main__":
    line = input().split()
    print(new_xor(int(line[0]), int(line[1])))


