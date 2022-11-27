# set with specific element
def find_parent(parent, x):
  # if not root, call recursion
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
    
n, m = map(int, input().split())
# initialization
parent = [0] * (n+1)

# initialize with self
for i in range(0, n+1):
  parent[i] = i
  
# check each operation
for i in range(m):
  oper, a, b = map(int, input().split())
  # union
  if oper == 0:
    union_parent(parent, a, b)
  # find
  elif oper == 1:
    if find_parent(parent, a) == find_parent(parent, b):
      print('YES')
    else:
      print('NO')
