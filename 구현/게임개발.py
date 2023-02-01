# Receive N, M
n, m = map(int, input().split())

# Initialize history map
d = [[0] * m for _ in range(n)]
# Receive X, Y, direction
x, y, direction = map(int, input().split())
# Check current location as 'visited'
d[x][y] = 1 

# Receive entire map information
array = []
for i in range(n):
  array.append(list(ap(int, input().split())))
  
# North, East, South, West
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# turn left
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3
    
 # Start simulation
count = 1
turn_time = 0
while True:
  # turn left
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # move to unexplored front cell 
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  # cannot move to already explored front cell or sea
  else:
    turn_time += 1
  # cannot move to all direction
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    # move back if we can
    if array[nx][ny] == 0:
      x = nx
      y = ny
    # if back is the sea
    else:
      break
     turn_time = 0
    
  print(count)
