from itertools import combinations
def solution(numbers):
    pair = combinations(numbers, 2)
    prod = [x[0]*x[1] for x in pair]
    answer = max(prod)
    return answer
