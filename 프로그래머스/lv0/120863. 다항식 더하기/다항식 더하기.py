def solution(polynomial):
    a = []
    b = []
    for i in polynomial.split():
        if 'x' == i:
            a.append(int(i.replace('x', '1')))
        elif 'x' in i:
            a.append(int(i.replace('x', '')))
        elif i.isdigit():
            b.append(int(i))

    if len(a) > 0 and len(b) > 0:
        if sum(a) == 1:
            answer = f'x + {sum(b)}'
        else:
            answer = f'{sum(a)}x + {sum(b)}'
    elif len(a) == 0:
        answer = f'{sum(b)}'
    elif len(b) == 0:
        if sum(a) == 1:
            answer = 'x'
        else:
            answer = f'{sum(a)}x'
    return answer