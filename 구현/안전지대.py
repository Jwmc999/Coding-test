def solution(board):
    n = len(board)
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                surr = []
                nx = [i+x for i in dx]
                ny = [i+y for i in dy]
                for i in range(8):
                    if 0<=nx[i]<n and 0<=ny[i]<n:
                        surr.append(board[nx[i]][ny[i]])
                if all(s==0 for s in surr):
                    cnt += 1
            else:
                continue
                        

    answer = cnt
    return answer
