from re import *

with open("1975.txt", "r") as f:
    data = f.readline()

pattern = r'[^P]*(P[^P]+)*P?'
# pattern = r'(P?[^P]+)+P?'

matches = [m.group() for m in finditer(pattern, data)]
print(matches)
answer = max(matches, key=len)
print(len(answer))
