# Перевод в 3-чную систему
def to_ternary(num):
    result = ''
    while num:
        result += str(num % 3)
        num //= 3
    return result[::-1]