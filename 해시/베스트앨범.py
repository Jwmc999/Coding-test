from collections import defaultdict
def solution(genres, plays):
    answer = []
    hash = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)): 
        hash[g].append((i, p))
        
    gen = dict()
    for k, v in hash.items():
        gen[k] = sum(m for _, m in v)
        
    keys = sorted(hash.items(), key=lambda kv: gen[kv[0]], reverse=True)
    keys = [x[0] for x in keys]

    for k in keys:      
        v = hash[k]
        v = sorted(v, key = lambda x: x[1] , reverse=True)
        s = [x[0] for x in v]
        answer.extend(s[:2])
        
    return answer
