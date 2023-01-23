from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    f = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    answer = [f.numerator, f.denominator]
    return answer
