def solution(bandage, health, attacks):
    answer = health
    attacks.append([0, 0])
    attacks.sort(key=lambda x: x[0])
    for i in range(len(attacks)-1):
        diff_t = attacks[i+1][0] - attacks[i][0]
        answer += ((diff_t-1) // bandage[0]) * bandage[2] + (diff_t-1) * bandage[1]
        if answer >= health:
            answer = health
        answer -= attacks[i+1][1]
        if answer <= 0:
            return -1 

    return answer