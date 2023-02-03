import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]
permu_arr = list(permutations(arr, m))

for j in permu_arr:
    print(*j)