if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(0, N):
        line = input().split()
        command = line[0]
        del line[0]
        if command == "insert":
            arr.insert(int(line[0]), int(line[1]))
        if command == "print":
            print(arr)
        if command == "remove":
            for i in range(0, len(arr)):
                if arr[i] == int(line[0]):
                    del arr[i]
                    break
        if command == "append":
            arr.append(int(line[0]))
        if command == "sort":
            arr.sort()
        if command == "pop":
            arr.pop(-1)
        if command == "reverse":
            arr.reverse()




