from re import *

with open("3584.txt", "r") as f:
    data = f.readline()

pattern = r'(BA|DA)+'
matches = [m.group() for m in finditer(pattern, data)]

answer = max(matches, key=len)
print(len(answer) / 2)
