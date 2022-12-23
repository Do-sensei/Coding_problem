arr = []
for i in range(5):
    n = int(input())
    arr.append(n)

arr.sort()
    
print(int(sum(arr)/5))
print(arr[len(arr)//2])