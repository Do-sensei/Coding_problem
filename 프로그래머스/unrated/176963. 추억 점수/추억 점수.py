def solution(name, yearning, photo):
    answer = []
    name_dic = {k:v for k, v in zip(name, yearning)}
    for n in photo:
        score = 0
        for j in n:
            if j in name:
                score += name_dic[j]
        answer.append(score)
    return answer