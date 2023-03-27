def solution(s):
    answer = True
    a = s.lower()
    lst_a = list(a)
    p, y = 0, 0
    for i in lst_a:
        if i == 'p':
            p += 1
        elif i == 'y':
            y += 1
    if p != y:
        answer = False
    return answer