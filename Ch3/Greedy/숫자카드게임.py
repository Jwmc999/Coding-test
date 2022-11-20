# Input of N, M
n, m = map(int, input().split())

result = 0
# receive input line by line
for i in range(n):
  data = list(map(int, input().split()))
  # find smallest number from current line
  min_value = min(data)
  # find largest number from smallest numbers
  result = max(result, min_value)
  
# result
print(result)
