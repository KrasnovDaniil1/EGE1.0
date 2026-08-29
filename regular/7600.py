from re import *

with open("7600.txt", "r") as f:
    data = f.readline()

pattern = r'[^QRS]*([QRS][^QRS]+)+[QRS]?'
matches = [m.group() for m in finditer(pattern, data)]

answer = max(matches, key=len)
print(len(answer))
