def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    m_arr = []
    for i in range(0, len(score), m):
        if len(score[i:i+m]) == m:
            m_arr.append(score[i:i+m])
    for j in m_arr:
        answer += min(j) * m
    return answer 