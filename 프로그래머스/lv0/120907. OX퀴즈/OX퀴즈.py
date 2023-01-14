def solution(quiz):
    answer = []
    for i in quiz:
        a = i.split("=")
        if eval(a[0]) == int(a[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer