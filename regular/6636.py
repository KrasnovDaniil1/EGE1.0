from re import *

with open("6636.txt", "r") as f:
    data = f.readline()

pattern = r'([24][135])+'
matches = [m.group() for m in finditer(pattern, data)]

answer = max(matches, key=len)
print(len(answer) / 3)
