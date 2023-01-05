import sys

n, m = map(int, sys.stdin.readline().split())

arr_1 = [sys.stdin.readline() for _ in range(n)]
arr_2 = [sys.stdin.readline() for _ in range(m)]

cnt = 0

for i in arr_2:
    if i in arr_1:
        cnt += 1
        
print(cnt)