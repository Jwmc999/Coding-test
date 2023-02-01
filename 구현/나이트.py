# Receive current location
input_data = input()
row = int(input_data[1])
# ord: chr to ASCII code
column = int(ord(input_data[0])) - int(ord('a')) + 1 

# 8 positions of Knight
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# check if we can move to each position
result = 0
for step in steps:
  # check desired location
  next_row = row + step[0]
  next_column = column + step[1]
  # count if we can move to the position
  if next_row >=1 and next_row <= 8 and next_column >= 1 and next_column <=8:
    result += 1
    
print(result)
