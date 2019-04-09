if __name__ == '__main__':
    marklist = []
    for _ in range(0,int(input())):
        marklist.append([input(), float(input())])
    second = sorted(list(set([marks for name, marks in marklist])))[1]
    marklist.sort()
    for name, mark in marklist:
        if mark == second:
            print(name, end = '\n')


