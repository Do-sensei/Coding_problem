n = int(input())
arr = list(map(int, input().split()))
comp = []

arr_ord = sorted(list(set(arr)))
arr_dic = {k:i for i, k in enumerate(arr_ord)}

for j in arr:
    comp.append(arr_dic.get(j))

print(*comp)