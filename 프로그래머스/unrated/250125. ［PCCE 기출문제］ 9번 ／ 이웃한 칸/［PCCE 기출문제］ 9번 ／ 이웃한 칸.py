def solution(board, h, w):
    answer = 0
    pad_board = [[0] * (len(board)+2) for _ in range(len(board)+2)]
    pad_board[1:-1] = [[0] + i + [0] for i in board]
    for i in [-1, 1]:
        if pad_board[h+1+i][w+1] == pad_board[h+1][w+1]:
            answer += 1
        if pad_board[h+1][w+1+i] == pad_board[h+1][w+1]:
            answer += 1
    return answer