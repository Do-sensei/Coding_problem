while True:
    arr = list(map(int, input().split()))
    max_a = max(arr)
    if sum(arr) == 0:
        break
    arr.remove(max_a)
    if (arr[0]**2) + (arr[1]**2) == (max_a**2):
        print('right')
    else:
        print('wrong')