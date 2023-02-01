def factorization(x):
    divsor = []
    d = 2
    while d <= x:
        if x % d == 0:
            divsor.append(d)
            x /= d
        else:
            d += 1
    return sorted(list(set(divsor)))

def solution(n):
    answer = factorization(n)
    return answer
