def solution(my_string, n):
    tmp = ''
    for s in my_string:
        for e in s:
            tmp += e*n
    answer = tmp
    return answer
