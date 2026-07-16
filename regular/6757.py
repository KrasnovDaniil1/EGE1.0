from re import *

with open("6757.txt", "r") as f:
    data = f.readline()

pattern = r'(CFE|FCE)+'
matches = [m.group() for m in finditer(pattern, data)]

answer = max(matches, key=len)
print(len(answer) / 3)
