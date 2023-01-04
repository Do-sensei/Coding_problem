n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input())

draw = []
for i in range(n-7):
    for j in range(m-7):
        start_b = 0
        start_w = 0
        
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if arr[k][l] != 'B':
                        start_b += 1
                    if arr[k][l] != 'W':
                        start_w += 1
                else:
                    if arr[k][l] != 'W':
                        start_b += 1
                    if arr[k][l] != 'B':
                        start_w += 1
        
        draw.append(start_b)
        draw.append(start_w)

print(min(draw))