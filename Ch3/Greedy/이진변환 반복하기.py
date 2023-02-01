# 재귀 문제
def reducer(s, cnt=0, zeros=0):
    string = [x for x in s]
    # count 0
    zeros += string.count('0')
    print(zeros)
    # remove 0
    string = [x for x in string if x!='0']
    # to binary
    string = ''.join(string)
    binary = str(bin(len(string))[2:])
    # count iteration
    cnt += 1    
    if binary != '1':
        return reducer(binary, cnt, zeros)
    else:
        return [cnt, zeros]

def solution(s):
    answer = reducer(s)
    return answer
