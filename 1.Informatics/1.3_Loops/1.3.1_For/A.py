a = int(input())
b = int(input())
min_a = a
if a % 2 == 1 :
    min_a = a + 1
for index in range(min_a, b + 1, 2):
    print(str(index), end = " ")
