from collections import Counter
def solution(s):
    answer = ''
    arr = []
    for i in s:
        arr.append(i)
    arr.sort()
    s_dic = Counter(arr)
    for k, v in s_dic.items():
        if v == 1:
            answer += k
    
    return answer