n = [list(map(int, input().split())) for _ in range(9)]

max_row = []
for row in n:
    max_row.append(max(row))
max_a = max(max_row)
print(max_a)
for r, i in enumerate(n):
    for c, j in enumerate(i):
        if j == max_a:
            print(r+1, c+1)