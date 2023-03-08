def solution(n):
    melon = ['수', '박']
    answer = ''
    for i in range(n):
        answer += melon[i%2]
    return answer