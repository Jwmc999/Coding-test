def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)

    for number, p in zip(phone_book, phone_book[1:]):
        if p.startswith(number):
            answer=False
            break
    return answer
