from string import ascii_lowercase
def solution(age):
    age_alph = {str(k): v for k,v in  zip(range(10), ascii_lowercase)}
    answer =''
    for i in str(age):
        answer += age_alph[i]
    return answer