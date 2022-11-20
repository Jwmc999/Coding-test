# Receive N, M
n, m = map(int, input().split())

# Receive 2D array
graph = []
for i in range(n):
  graph.append(list(map(int, input.split())))
  
# DFS: visit the specific node and then also visit all neighboring nodes
def dfs(x, y):
  # terminate when out of range
  if x <= -1 or x >= n or y <=-1 or y >= m:
    return False
  # not explored current node yet
  if graph[x][y] == 0:
    # check current node
    graph[x][y] = 1
    # up, down, left, right 
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False

# fill all nodes with drink
result = 0
for i in range(n):
  for j in range(m):
    # DFS at current location
    if dfs(i, j) == True:
      result += 1
      
print(result)
