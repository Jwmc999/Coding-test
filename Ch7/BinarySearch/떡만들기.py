# receive N (number), M (length)
n, m = list(map(int, input().split(' ')))
# Receive height
array = list(map(int, input().split()))

# start and end of binary search
start = 0
end = max(array)

# binary search
result = 0
while(start <= end):
  total = 0
  mid = (start + end) // 2
  for x in array:
    # amount after divide
    if x > mid:
      total += x - mid
  # left search
  if total < m:
    end = mid - 1
  # right search
  else:
    result = mid
    start = mid + 1
    
print(result)
 
