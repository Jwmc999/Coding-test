from collections import deque

# Receive N, M
n, m = map(int, input().split())
# Receive 2D map
graph = []
for i in range(n):
  graph.append(list(map(int, input())))
  
# 4 directions: up, down, left, right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def bfs(x, y):
  # Queue
  queue = deque()
  queue.append((x, y))
  # loop till queue is empty
  while queue:
    x, y =  queue.popleft()
    # check 4 directions
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # ignore when out of range
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      # ignore if wall
      if graph[nx][ny] == 0:
        continue
      # count shortest path only for the first visit to the node.
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  # return shortest path to the lowest right 
  return graph[n-1][m-1]

print(bfs(0, 0))
