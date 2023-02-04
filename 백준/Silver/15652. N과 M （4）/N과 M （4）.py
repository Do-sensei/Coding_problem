import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]
cwr_arr = list(combinations_with_replacement(arr, m))

for j in cwr_arr:
    print(*j)