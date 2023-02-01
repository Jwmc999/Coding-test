def solution(array):
    answer = [sorted(array, reverse=True)[0], array.index(sorted(array, reverse=True)[0])]
    return answer
