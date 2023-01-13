n = int(input())

for _ in range(n):

    arr = list(map(int, input().split()))
    coord = ((arr[0] - arr[3])**2 + (arr[1] - arr[4])**2)**0.5
    dist_1 = arr[2] + arr[5]
    dist_2 = abs(arr[2] - arr[5])
    
    if coord == 0:
        if arr[2] == arr[5]:
            print(-1)
        else:
            print(0)
    elif dist_2 < coord < dist_1:
        print(2)
    elif coord == dist_1 or coord == dist_2:
        print(1)
    else:
        print(0)