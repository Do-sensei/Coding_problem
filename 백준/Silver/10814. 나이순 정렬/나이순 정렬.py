n = int(input())
arr = []

for _ in range(n):
    m, l = input().split()
    m = int(m)
    arr.append((m, l))

arr.sort(key= lambda x : x[0])

for i in arr:
    print(i[0], i[1])