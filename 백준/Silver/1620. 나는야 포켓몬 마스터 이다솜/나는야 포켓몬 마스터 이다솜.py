import sys
input = sys.stdin.readline

n, m = map(int, input().split())

collection = {}

for i in range(n):
    o = input().rstrip()
    collection[i+1] = o
    collection[o] = i+1
    
for _ in range(m):
    p = input().rstrip()
    if p.isdigit():
        print(collection[int(p)])
    else:
        print(collection[p])

