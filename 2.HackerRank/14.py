
def swap_case(s):
    arr = ""
    for ch in s:
        if ord(ch) in range(65, 91):
            arr += (chr(ord(ch) + 32))
        elif ord(ch) in range(97, 123):
            arr += (chr(ord(ch) - 32))
        else:
            arr+= ch
    return arr


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)