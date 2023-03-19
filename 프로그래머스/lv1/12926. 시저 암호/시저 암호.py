from string import ascii_lowercase, ascii_uppercase
def solution(s, n):
    answer = ''
    for i in s:
        if i in ascii_lowercase:
            answer += ascii_lowercase[(ascii_lowercase.index(i)+n)%26]
        elif i in ascii_uppercase:
            answer += ascii_uppercase[(ascii_uppercase.index(i)+n)%26]
        else:
            answer += ' '
    return answer