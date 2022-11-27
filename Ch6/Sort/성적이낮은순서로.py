# Receive N
n = int(input())

# receive N student
array = []
for i in range(n):
  input_data = input().split()
  # name -> string, score -> int
  array.append((input_data[0], int(input_data[1])))
  
# sort by key=score
array = sorted(array, key=lambda student:student[1])

# print sorted result
for student in array:
  print(student[0], end=' ')
