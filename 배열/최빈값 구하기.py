from collections import Counter

def solution(array):
    cnt = Counter(array).most_common()
    if (len(cnt) > 1):
        if (cnt[0][1] == cnt[1][1]):
            answer = -1
        else:
            answer = cnt[0][0]
    else:
        answer = cnt[0][0]
        
    return answer
