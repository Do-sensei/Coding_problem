def solution(id_pw, db):
    answer = 'fail'
    for i in db:
        if id_pw == i:
            answer = 'login'
        elif id_pw[0] == i[0]:
            answer = 'wrong pw'

    return answer