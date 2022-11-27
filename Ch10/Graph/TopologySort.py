from collections import deque
import copy

# receive number of nodes
v = int(input())
# initialize indegree as 0
indegree = [0] * (v+1)
# initialize graph
graph = [[] for i in range(v+1)]
# initialize time as 0
time = [0] * (v+1)

# directed graph
for i in range(1, v+1):
  data = list(map(int, input().split()))
  # first number stores time info
  time[i] = data[0]
  for x in data[1:-1]:
    indegree[i] += 1
    graph[x].append(i)

# topology sort
def topology_sort():
  result = copy.deepcopy(time)
  q = deque()
  
  # insert node with 0 indegree to queue
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)
      
  # repeat until queue is empty
  while q:
    # pop element from queue
    now = q.popleft()
    # indgree - 1 for connected nodes of the deleted element 
    for i in graph[now]:
      result[i] = max(result[i], result[now] + time[i])
      indegree[i] -= 1
      # insert node with indegree 0
      if indegree[i] == 0:
        q.append(i)
    
  # print result
  for i in range(1, v+1):
    print(result[i])
    
 topology_sort()
