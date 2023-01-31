def dfs (index, computers, explored):
    if (explored[index]):
        return 0
    else:
        explored[index] = True
        for i in range(0, len(computers)):
            if (computers[index][i] == 1):
                dfs(i,computers,explored)
        return 1

def solution(n, computers):
    answer = 0
    explored = []
    for i in range(0, n):
        explored.append(False)
    for index in range(0, n):
        answer += dfs(index, computers, explored)

    return answer
