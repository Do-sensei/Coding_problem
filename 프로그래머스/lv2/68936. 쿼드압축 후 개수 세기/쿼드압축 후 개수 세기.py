def compress(x, y, n, arr):

    if all([arr[i][j] == arr[x][y] for i in range(x, x+n) for j in range(y, y+n)]):
        return [0, 1] if arr[x][y] == 1 else [1, 0]
    
    half = n // 2
    top_left = compress(x, y, half, arr)
    top_right = compress(x, y+half, half, arr)
    bottom_left = compress(x+half, y, half, arr)
    bottom_right = compress(x+half, y+half, half, arr)
    
    return [sum(x) for x in zip(top_left, top_right, bottom_left, bottom_right)]

def solution(arr):
    return compress(0, 0, len(arr), arr)
