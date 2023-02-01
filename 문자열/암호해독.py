def solution(cipher, code):
    answer = ''
    for i, c in enumerate(cipher):
        if (i+1)%code==0:
            answer += c

    return answer
