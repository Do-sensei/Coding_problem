n = int(input())
arr = list(map(int, input().split()))
ref = int(input())

cnt = 0
for i in arr:
    if ref == i:
        cnt += 1

print(cnt)