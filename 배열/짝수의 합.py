def solution(n):
    even = [2*i for i in range(int(n//2)+1)]
    answer = sum(even)
    return answer
