# Receive X
x = int(input())

# memoization
d = [0] * 30001

# Dynamic programming (bottom up)
for i in range(2, x + 1):
  # current value - 1
  d[i] = d[i-1] + 1
  # current value % 2 == 0
  if i % 2 == 0:
    d[i] = min(d[i], d[i//2] + 1)
  # current value % 3 == 0
  if i % 3 == 0:
    d[i] = min(d[i], d[i//3] + 1)
  # current value % 5 == 0
  if i % 5 == 0:
    d[i] = min(d[i], d[i//5] + 1)

print(d[x])
