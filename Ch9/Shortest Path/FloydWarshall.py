INF = int(1e9)

# number of node, number of edge
n, m = map(int, input().split())
# create and initialize 2D list
graph = [[INF] * (n+1) for _ in range(n+1)]

# from self to self
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0
      
# receive each edge
for _ in range(m):
  # A to B, B to A = 1
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1
  
# x: visiting node. k: target node
x, k = map(int, input().split())

# Floyd Warshall algorithm
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
      
# print result
distance = graph[1][k] + graph[k][x]

# if cannot be reached, -1
if distance >= INF:
  print("-1")
# if can be reached, print shortest path
else:
  print(distance)
