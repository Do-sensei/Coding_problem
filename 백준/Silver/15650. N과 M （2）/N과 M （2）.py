import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]
permu_arr = list(combinations(arr, m))

for j in permu_arr:
    print(*j)