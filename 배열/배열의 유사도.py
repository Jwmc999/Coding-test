def solution(s1, s2):
    common = set(s1).intersection(set(s2))
    answer = len(common)
    return answer
