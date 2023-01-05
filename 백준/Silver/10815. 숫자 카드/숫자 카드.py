import sys

n = int(sys.stdin.readline())
arr_1 = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
arr_2 = list(map(int, sys.stdin.readline().split()))

for i in arr_2:
    if i in arr_1:
        print(1, end=' ')
    else:
        print(0, end=' ')