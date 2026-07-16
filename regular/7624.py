from re import *

with open("7624.txt", "r") as f:
    data = f.readline()

data = ""

pattern = r''
matches = [m.group() for m in finditer(pattern, data)]

answer = max(matches, key=len)
print(len(answer))
