from collections import Counter
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(input().rstrip())

for _ in range(m):
    arr.append(input().rstrip())    

arr.sort()
cnt = Counter(arr)
result = []

for k, v in cnt.items():
    if v == 2:
        result.append(k)
        
print(len(result))
for i in result:
    print(i)