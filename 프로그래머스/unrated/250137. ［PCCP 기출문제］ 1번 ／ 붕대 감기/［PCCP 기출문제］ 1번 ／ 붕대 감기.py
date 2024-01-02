def solution(bandage, health, attacks):
    answer = health
    t, x, y = bandage
    attacks.append([0, 0])
    attacks.sort(key=lambda x: x[0])
    for i in range(len(attacks)-1):
        diff_att_t = attacks[i+1][0] - attacks[i][0] - 1

        answer += ((diff_att_t) // t) * y + (diff_att_t) * x
        answer = min(answer, health)

        answer -= attacks[i+1][1]

        if answer <= 0:
            return -1 

    return answer