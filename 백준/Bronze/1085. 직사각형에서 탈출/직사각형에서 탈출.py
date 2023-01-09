arr = list(map(int, input().split()))

tri_len = [arr[0], arr[1], arr[2]-arr[0], arr[3]-arr[1]]

print(min(tri_len))
