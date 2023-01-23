import math

def lcm(a, b):
    return ( a * b) // math.gcd(a,b)

def solution(n):
    if n%6==0:
        answer = n//6
    else:
        answer = lcm(n, 6) // 6
    return answer
