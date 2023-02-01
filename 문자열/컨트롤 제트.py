def solution(s):
    s = s.split(' ')
    s = ['-'+s[i-1] if j=='Z' else j for i, j in enumerate(s)]
    s = [c.replace('--', '') for c in s]
    s = [int(x) for x in s]
    answer = sum(s)
    return answer
