# 같은 등수는 그 등수 숫자를 건너뛰고 계산
def solution(score):
    score = [x[0]+x[1] for x in score]
    answer = [sorted(score, reverse=True).index(x)+1 for x in score]
    return answer
