import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_ls = list(range(1, n+1))

for _ in range(m):
    i, j = map(int, input().split())
    n_ls[i-1:j] = n_ls[i-1:j][::-1]

print(' '.join(map(str, n_ls)))