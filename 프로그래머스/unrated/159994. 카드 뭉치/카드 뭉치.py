def solution(cards1, cards2, goal):
    answer = 'Yes'
    c1_cnt = 0
    c2_cnt = 0
    for i in goal:
        if i in cards1:
            if c1_cnt != cards1.index(i):
                answer = 'No'
                break
            else:
                c1_cnt +=1
        else:
            if c2_cnt != cards2.index(i):
                answer = 'No'
                break
            else:
                c2_cnt +=1

    return answer