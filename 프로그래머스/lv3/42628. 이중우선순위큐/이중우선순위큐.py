def solution(operations):
    answer = []

    for i in operations:
        if i[0] == 'I':
            answer.append(int(i[2:]))
        elif i[0] == 'D':
            if i[2:] == '1':
                try:
                    answer.remove(max(answer))
                except:
                    pass
            elif i[2:] == '-1':
                try:
                    answer.remove(min(answer))
                except:
                    pass

    if len(answer) == 0:
        answer = [0, 0]
    else:
        answer = [max(answer), min(answer)]

    return answer