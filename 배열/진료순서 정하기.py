def solution(emergency):
    tmp = sorted(emergency, reverse=True)
    return [tmp.index(e)+1 for e in emergency]
