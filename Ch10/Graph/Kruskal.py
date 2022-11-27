# find parent
def find_parent(parent, x):
  # if not root, call recursively
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# combine two sets
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
    
# number of node, number of edge
v, e = map(int, input().split())
# initialize parent table
parent = [0] * (v+1)

edges = []
result = 0

# initialize as self
for i in range(1, v+1):
  parent[i] = i
  
# receive all edges
for _ in range(e):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))
  
# sort edges by cost
edges.sort()
# for edges in minimum spanning tree, edge with biggest cost
last = 0

# check each edge
for edge in edges:
  cost, a, b = edge
  # only include acyclic
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
    last = cost
    
print(result - last)
