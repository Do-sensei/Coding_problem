def solution(s):
    answer = ''
    arr = list(s.split(' '))
    for i in range(len(arr)):
        if i  > 0 :
            answer += ' '
        for j in range(len(arr[i])):
            if j % 2 == 0:
                answer += arr[i][j].upper()
            else:
                answer += arr[i][j].lower()
    print(arr)
    return answer