# binary search
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    # if you found target
    if array[mid] == target:
      return mid
    # if target < median, check left
    elif array[mid] > target:
      end = mid - 1
    # if target > median, check right
    else:
      start = mid + 1
  return None

# Receive N (number of components)
n = int(input())
# Receive entire component codes
array = list(map(int, input().split()))
# sort array for binary search
array.sort()
# Receive M (number of requested components)
m = int(input())
# Receive entire component codes == targets
x = list(map(int, input().split()))

# check target codes one by one
for i in x:
  # check if the component exists
  result = binary_search(array, i, 0, n-1)
  if result != None:
    print('yes', end = ' ')
  else:
    print('no', end = ' ')
