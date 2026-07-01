from itertools import *

letter = sorted("АЛГОРИТМ")
for pos, val in enumerate(product(letter, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] != "А" and val[0] != "Г" and val.count("Р") >= 2:
        print(pos)
        break

# print(8626)