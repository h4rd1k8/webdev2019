if __name__ == '__main__':
    n = int(input())
    arr = [int(number) for number in input().split()]
    arr.sort(reverse = True)
    for i in range(0, len(arr) - 1):
        if arr[i] != arr[i + 1]:
            print(arr[i + 1])
            break

