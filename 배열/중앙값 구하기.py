def solution(array):
    array = sorted(array, reverse=False)
    i = (len(array) + 1)//2 
    answer = array[i-1]
    return answer
