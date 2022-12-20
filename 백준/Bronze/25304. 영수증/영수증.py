n = int(input())
m = int(input())
arr = []
total = 0
for _ in range(m):
    arr.append(list(map(int, input().split())))

for i in arr:
    total += i[0] * i[1]

if total == n:
    print('Yes')
else:
    print('No')    