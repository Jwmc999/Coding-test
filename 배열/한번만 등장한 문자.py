from collections import Counter
def solution(s):
    pair = [k for k, v in Counter(s).items() if v == 1]
    pair.sort()
    answer = ''.join(pair)
    return answer
