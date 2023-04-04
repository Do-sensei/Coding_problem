from collections import Counter

def solution(k, tangerine):
    answer = 0
    cnt = Counter(tangerine)
    sorted_cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    cnt_tang = 0
    for i in range(len(sorted_cnt)):
        if cnt_tang < k:
            cnt_tang += sorted_cnt[i][1]
            answer += 1
        else:
            break
    return answer