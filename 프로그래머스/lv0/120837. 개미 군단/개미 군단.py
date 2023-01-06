def solution(hp):
    answer = 0
    while hp % 5 != 0:
        answer += 1
        hp -= 3
    answer += hp//5
    return(answer)