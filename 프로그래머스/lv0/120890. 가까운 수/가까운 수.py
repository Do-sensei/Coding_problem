def solution(array, n):
    min_n = 100
    arr = []
    for i in range(len(array)):
        if abs(n - array[i]) < min_n:
            min_n = abs(n - array[i])
    
    for j in range(len(array)):
        if abs(n - array[j]) == min_n:
            arr.append(array[j])
    arr.sort()
    answer = arr[0]
    return answer