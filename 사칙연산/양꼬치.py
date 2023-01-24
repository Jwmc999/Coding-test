def solution(n, k):
    mok = n//10
    # namuji = n % 10
    
    answer = n*12000+(k-mok)*2000
    return answer
