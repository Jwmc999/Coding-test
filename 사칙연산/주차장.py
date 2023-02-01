from collections import defaultdict
import math
def solution(fees, records):
    basetime, basefee, unittime, unitfee = fees
    
    queue = defaultdict(list)
    for rec in records:
        time, num, act = rec.split(' ')
        h, m = time.split(':')
        whole = int(h) * 60 + int(m)
        queue[num].append((whole, act))

    for k, v in queue.items():
        IN = [x[0] for x in v if x[1]=='IN']
        OUT = [x[0] for x in v if x[1]=='OUT']
        if len(IN) > len(OUT):
            OUT = OUT + [23*60+59] * (len(IN)-len(OUT))
        use = [o-i for i, o in zip(IN, OUT)]
        if sum(use) < basetime:
            queue[k] = basefee
        else:
            queue[k] = basefee + math.ceil((sum(use) - basetime)/unittime) * unitfee
    answer = [x[1] for x in sorted(queue.items(), key = lambda v: v[0])]
    return answer
