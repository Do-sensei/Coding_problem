n = int(input())
arr = []

for _ in range(n):
    m = input()
    arr.append(m)
    
arr = list(set(arr))
arr.sort()
arr_dic = {k:len(k) for k in arr}
arr_dic = sorted(arr_dic.items(), key= lambda x : x[1])
for i in arr_dic:
    print(i[0])