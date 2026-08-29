from re import *

with open("24374.txt", "r") as f:
    data = f.readline()

pattern = r'[0-9]*[A-Z]+([0-9]+[A-Z]+){79}[0-9]*'

matches = [m.group() for m in finditer(pattern, data)]
print(matches)
answer = max(matches, key=len)
print(data.find(answer))

