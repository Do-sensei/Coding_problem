n = int(input())
arr = []
for _ in range(n):
    m = list(map(int, input().split()))
    arr.append(m)
arr_rank = [1 for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            arr_rank[i] += 1
        elif arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            arr_rank[j] += 1

print(*arr_rank)