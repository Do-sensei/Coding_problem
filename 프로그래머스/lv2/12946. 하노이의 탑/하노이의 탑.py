
def hanoi(n, one, two, three, answer=[]):
    if n == 1:
        answer.append([one, three])
        return answer
    hanoi(n-1, one, three, two, answer)
    answer.append([one, three])
    hanoi(n-1, two, one, three, answer)
    return answer

def solution(n):
    return hanoi(n, 1, 2, 3)
