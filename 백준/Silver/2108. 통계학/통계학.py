from collections import Counter
import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    m = int(sys.stdin.readline())
    arr.append(m)

arr.sort()
cnt = Counter(arr).most_common()

print(round(sum(arr)/n))
print(arr[n//2])
if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(arr[-1] - arr[0])