def solution(bin1, bin2):
    answer = ''
    a, b = int(bin1, 2), int(bin2, 2)
    c = bin(a+b)[2:]

    answer += str(c)
    return answer