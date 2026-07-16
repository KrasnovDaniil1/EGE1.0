from re import *

with open("9791.txt", "r") as f:
    data = f.readline()

pattern = r'([0-9A-F])*'
matches = [m.group() for m in finditer(pattern, data)]

answer = max(matches, key=len)
print(len(answer))
