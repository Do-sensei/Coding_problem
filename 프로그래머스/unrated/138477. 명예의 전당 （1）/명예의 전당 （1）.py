def solution(k, score):
    answer = []
    arr = []
    for i in range(len(score)):
        if i < k:
            arr.append(score[i])
            arr.sort(reverse=True)
            answer.append(arr[-1])
        else:
            arr.append(score[i])
            arr.sort(reverse=True)
            answer.append(arr[k-1])
    return answer