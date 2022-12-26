n = [i for i in input()]
n.sort(reverse=True)
arr = []
for j in n:
    arr.append(j)

for j in arr:
    print(j, end='')