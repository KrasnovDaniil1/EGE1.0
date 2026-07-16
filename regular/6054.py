from re import *

with open("6054.txt", "r") as f:
    data = f.readline()

# pattern = r'([BC][BC]A)+'
pattern = r'([^A][^A]A)+'
matches = [m.group() for m in finditer(pattern, data)]

answer = max(matches, key=len)
print(len(answer))
