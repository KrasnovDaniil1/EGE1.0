from re import *

with open("6029.txt", "r") as f:
    data = f.readline()

# data = "FEFE*EFEF*FEF*EFE"

pattern = r'(FE)+F?|(EF)+F?'
matches = [m.group() for m in finditer(pattern, data)]

answer = max(matches, key=len)
print(len(answer))
