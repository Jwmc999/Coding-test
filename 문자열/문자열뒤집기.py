def solution(my_string):
    ms = []
    ms[:0] = my_string
    ms = ms[::-1]
    answer = ''.join(ms)
    return answer
