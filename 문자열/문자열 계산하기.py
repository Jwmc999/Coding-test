def solution(my_string):
    string =  my_string.split(' ')
    answer = int(string[0])
    for i, s in enumerate(string):
        if s == '+':
            answer += int(string[i+1])
        elif s == '-':
            answer -= int(string[i+1]) 
        else:
            pass
    return answer
