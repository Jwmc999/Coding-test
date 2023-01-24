def solution(today, terms, privacies):
    h = {}
    for t in terms:
        h[t[0]] = int(t[1:])
    privacies = [(d[:-2], d[-1]) for d in privacies]
    answer = []
    for i, p in enumerate(privacies):
        tmp = p[0].split('.')
        today = today.split('.')
        tmp2 = [int(t) for t in tmp]
        tmp2[1] += h[p[1]]
        if tmp2[1] > 12:
            tmp2[0] += tmp2[1] // 12 
            tmp2[1] = tmp2[1] % 12
        if tmp2[1] < 10:
            tmp2[1] = '0' + str(tmp2[1])
        if tmp2[2] < 10:
            tmp2[2] = '0' + str(tmp2[2])
        if tmp2[1] == '00':
            tmp2[0] -= 1
            tmp2[1] = '12'
        if tmp2[2] == '00':
            tmp2[2] = '28'
        tmp2 = ''.join([str(t) for t in tmp2])
        today = ''.join([str(d) for d in today])
        if tmp2 <= today:
            answer.append(i+1)

    return answer
