from re import *

with open("3228.txt", "r") as f:
    data = f.readline()

pattern = r'(AC|AB)+'
matches = [m.group() for m in finditer(pattern, data)]

answer = max(matches, key=len)
print(len(answer) / 2)
