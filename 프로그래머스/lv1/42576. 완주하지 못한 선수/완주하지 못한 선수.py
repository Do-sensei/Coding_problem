from collections import Counter
def solution(participant, completion):
    answer = ''
    p, c = Counter(participant), Counter(completion)

    for k, v in c.items():
        p[k] -= v

    for k_p, v_p in p.items():
        if v_p == 1:
            answer = k_p
    return answer