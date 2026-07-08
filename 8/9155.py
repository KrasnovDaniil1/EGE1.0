from itertools import *

letter = sorted("АПРЕЛЬ",reverse=True)

cnt = 0
for pos, val in enumerate(product(letter, repeat = 5)):
    val = "".join(val)
    if val[-1] == "Ь" and pos <= 387:
        cnt += 1

print(cnt)
# print(65)