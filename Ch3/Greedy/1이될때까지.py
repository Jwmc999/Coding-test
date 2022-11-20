# Input of N, K
n, k = map(int, input().split())
result = 0

while True:
  # minus 1 until (N % K == 0)
  target = (n//k) * k
  result += (n-target)
  n = target
  # exit loop when N < K
  if n < k:
    break
  # divide by K
  result += 1
  n //= k
  
# minus 1 on remaining number
result += (n-1)

print(result)
