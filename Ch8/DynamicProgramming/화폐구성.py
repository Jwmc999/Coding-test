# Receive N, M
n, m = map(int, input().split())
# Receive currency unit for N
array = []
for i in range(n):
  array.append(int(input()))
  
# memoization
d = [10001] * (m+1)

# Dynamic programming (bottom up)
d[0] = 0
for i in range(n):
  for j in range(array[i], m+1):
    # if (i - k) is possible
    if d[j - array[i]] != 10001: 
      d[j] = min(d[j], d[j - array[i]] + 1)
      
# print result
# if M is impossible
if d[m] == 10001:
  print(-1)
else:
  print(d[m])
