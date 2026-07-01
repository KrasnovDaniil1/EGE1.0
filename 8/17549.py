from itertools import *

letter = sorted("ФОКУС")
for pos, val in enumerate(product(letter, repeat=5), start=1):
    val = ''.join(val)
    if val.count("У") == 2 and val.count("Ф") == 0:
        print(pos)

# print("2313")