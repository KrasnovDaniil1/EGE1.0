from itertools import *

letter = sorted("ПИТОН")
cnt = 0
for val in product(letter, repeat=4):
    val = ''.join(val)
    for g in "ИО":
        val = val.replace(g, "*")
    for g in "ПТН":
        val = val.replace(g, ".")

    if val.count('**') == 0 and val.count('..') == 0:
        cnt += 1
print(cnt)

# print(72)