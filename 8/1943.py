from itertools import *

cnt = 0
alph = sorted('ЗЕРКАЛО')
for val in product(alph, repeat=6):
    val = ''.join(val)
    if 1 <= val.count('К') <= 4:
        val = val.replace('К', '')
        if len(val) == len(set(val)):
            cnt += 1

print(cnt)
# print(12570)