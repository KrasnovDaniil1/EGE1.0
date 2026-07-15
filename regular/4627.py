from re import *

with open("4627.txt", "r") as f:
    data = f.readline()

pattern = r'(NPO|PNO)+'
matches = [m.group() for m in finditer(pattern, data)]

answer = max(matches, key=len)
print(len(answer) / 3)
