def solution(my_string):
    answer = ''.join(s.upper() if s.islower() else s.lower() for s in my_string)
    return answer
