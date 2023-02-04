import sys
from itertools import product
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]
product_arr = list(product(arr, repeat = m))

for j in product_arr:
    print(*j)