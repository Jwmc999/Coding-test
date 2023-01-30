def h(arr):
    if sum(arr) == 0:
        return 0
    else:
        array = [i+1 for i, j in enumerate(arr) if (j >= i+1)]
        return max(array)

def solution(citations):
    citations.sort(reverse=True)    
    answer = h(citations)
    return answer
