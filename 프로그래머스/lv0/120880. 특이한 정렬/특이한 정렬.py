def solution(numlist, n):
    answer = []
    num_dic = {}
    for i in numlist:
        num_dic[i] = abs(n-i)
    # num_dic = sorted(num_dic.items())
    num_dic = sorted(num_dic.items())
    num_dic = sorted(num_dic, key=lambda x: x[1], reverse=True)
    
    for i in reversed(num_dic):
        answer.append(i[0])
    return answer