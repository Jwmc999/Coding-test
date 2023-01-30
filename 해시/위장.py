from collections import defaultdict
import math
def solution(clothes):
    hash = defaultdict(list)
    for cloth in clothes: 
        hash[cloth[1]].append(cloth[0])
    
    value = hash.values()
    value = [len(v)+1 for v in value]
    return math.prod(value)-1
