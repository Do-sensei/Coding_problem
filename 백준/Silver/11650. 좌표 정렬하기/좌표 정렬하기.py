n = int(input())
arr = []

for _ in range(n):
    m, l = map(int, input().split())
    arr.append([m, l])

arr.sort()
for i in arr:
    print(i[0], i[1])