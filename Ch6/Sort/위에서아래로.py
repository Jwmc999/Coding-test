# Receive input
n = int(input())

# Receive N integers
array = []
for i in range(n):
  array.append(int(input()))
  
# sort
array = sorted(array, reverse=True)

# print sorted result
for i in array:
  print(i, end=' ')
