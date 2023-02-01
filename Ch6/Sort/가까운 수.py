def solution(array, n):
    array.sort()
    arr = [abs(i-n) for i in array]
    answer = array[arr.index(min(arr))]
    return answer
