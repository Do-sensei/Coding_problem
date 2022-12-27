n = int(input())
arr = []

for _ in range(n):
    m, l = map(int, input().split())
    arr.append([l, m])
    
arr.sort()
for i in arr:
    print(i[1], i[0])