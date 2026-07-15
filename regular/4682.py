from re import *

with open("4682.txt", "r") as f:
    data = f.readline()

pattern = r'([AE][BCD])*'
matches = [m.group() for m in finditer(pattern, data)]

answer = max(matches, key=len)
print(len(answer) / 2)
