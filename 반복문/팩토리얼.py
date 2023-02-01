import math
def solution(n):
    answer = 0
    facto = [(i, math.factorial(i)) for i in range(10, 0, -1)]
    for f in facto:
        if n >= f[1]:
            return f[0]
