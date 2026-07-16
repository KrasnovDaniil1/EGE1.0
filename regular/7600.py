from re import *

with open("7600.txt", "r") as f:
    data = f.readline()

data = "QRS*QRQR*QSQS*RSRS"

pattern = r''
matches = [m.group() for m in finditer(pattern, data)]

answer = max(matches, key=len)
print(len(answer))
