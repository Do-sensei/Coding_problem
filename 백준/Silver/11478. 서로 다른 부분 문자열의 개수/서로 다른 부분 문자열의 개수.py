import sys
input = sys.stdin.readline

n = input().rstrip()
set_arr = set()

for i in range(len(n)):
    for j in range(i, len(n)):
        set_arr.add(n[i:j+1])

print(len(set_arr))
