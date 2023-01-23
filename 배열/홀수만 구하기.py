def solution(n):
    if n%2==0:
        array = [2*i-1 for i in range(1,int(n/2)+1)]
    else:
        array = [2*i-1 for i in range(1,int((n+1)/2)+1)]
    answer = array
    return answer
