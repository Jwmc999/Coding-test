import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# Receive number of nodes, number of edge, start node
n, m, start = map(int, input().split())
# create graph for connected nodes
graph = [[] for i in range(n+1)]
# initialize shortest path table with INF
distance = [INF] * (n+1)

# all edge information
for _ in range(m):
  x, y, z = map(int, input().split())
  # z = cost of x node to y node
  graph[x].append((y, z))
  
def dijkstra(start):
  # insert shortest path to the start node into queue
  heapq.heappush(q, (0, start))
  distance[start] = 0
  # if queue is not empty
  while q:
    # pop node with the shortest path
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    # check neighbor nodes of current node
    for i in graph[now]:
      cost = dist + i[1]
      # if visting current node is less expensive
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
        
# dijkstra algorithm
dijkstra(start)

# number of reachable nodes
count = 0
# shortest path to farthest reachable node
max_distance = 0
for d in distance:
  # if reachable
  if d != INF:
    count += 1
    max_distance = max(max_distance, d)
    
# count -1
print(count-1, max_distance)
    
