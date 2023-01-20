def solution(score):
    sum_score = []
    answer = []
    for i in score:
        sum_score.append(sum(i))
    ord_score = sorted(sum_score, reverse=True)
    for j in sum_score:
        answer.append(ord_score.index(j)+1)
    return answer