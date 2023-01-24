def solution(rsp):
    hash = {
        '2':'0',
        '0':'5',
        '5':'2'
    }
    
    answer = ''.join(hash[s] for s in rsp)
    return answer
