def solution(keyinput, board):
    board = [board[0]//2, board[1]//2]
    answer = [0, 0]
    for i in keyinput:
        if i == "up" and board[1] > answer[1]:
            answer[1] += 1
        elif i == "down" and (-1 * board[1]) < answer[1]:
            answer[1] -= 1
        elif i == "right" and board[0] > answer[0]:
            answer[0] += 1
        elif i == "left" and (-1 * board[0]) < answer[0]:
            answer[0] -= 1
            
    return answer