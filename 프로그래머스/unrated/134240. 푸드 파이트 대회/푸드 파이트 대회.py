def solution(food):
    arr = []
    answer = ''
    for i in range(len(food)):
        if i == 0:
            arr.append('0')
        else:
            arr.append(f'{i}' * (food[i]//2))
            answer += f'{i}' * (food[i]//2)
    answer += arr[0]
    for j in range(len(arr)-1, 0, -1):
        answer += arr[j]
    # print(arr)
    return answer