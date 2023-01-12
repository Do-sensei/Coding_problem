def solution(num, k):
    answer = -1
    for a, i in enumerate(str(num)):
        if i == str(k):
            answer = a+1
            break
    return answer