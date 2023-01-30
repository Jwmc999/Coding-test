def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    
    lft = [x for x in tail if x<= pivot]
    rgt = [x for x in tail if x> pivot]
    
    return quick(lft) + [pivot] + quick(rgt)

def solution(array, commands):
    answer = []
    for command in commands:
        arr = array[command[0]-1:command[1]]
        arr = quick(arr)
        answer.append(arr[command[2]-1])
    return answer
