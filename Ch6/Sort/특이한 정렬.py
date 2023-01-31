def solution(numlist, n):
    numlst = [(num-n, abs(num-n)) for num in numlist]
    numlist = [abs(num-n) for num in numlist]
    numlst = sorted(numlst, key=lambda x: x[1])
    answer = [] 
    for num in numlst:
        if numlist.count(num[1]) > 1:
            answer.append(num[1])
            answer.append(num[1]*-1)
            numlst.remove(num)
        elif num[0]<0:
            answer.append(num[0])
        else:
            answer.append(num[0])
    answer = [a+n for a in answer]
    return answer
