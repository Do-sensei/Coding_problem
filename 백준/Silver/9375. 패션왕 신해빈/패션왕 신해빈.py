import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    arr = []
    for _ in range(m):
       _, a = input().split()
       arr.append(a)
    arr = Counter(arr)
    
    cnt = 1
    for k in arr:
        cnt *= arr[k] + 1
    print(cnt - 1) 