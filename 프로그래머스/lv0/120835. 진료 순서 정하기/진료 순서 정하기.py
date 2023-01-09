def solution(emergency):
    answer = []
    emer = sorted(emergency, reverse=True)
    emer_dic = {v: k+1 for k, v in enumerate(emer)}
    for i in emergency:
        answer.append(emer_dic[i])
    return answer