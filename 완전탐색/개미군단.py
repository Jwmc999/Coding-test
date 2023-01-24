def solution(hp):
    general = hp//5
    soldier = (hp - general * 5) // 3
    worker = hp - general * 5 - soldier * 3
    answer = general + soldier + worker
    return answer
