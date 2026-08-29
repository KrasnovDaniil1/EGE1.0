import re

with open(r"8837.txt") as f:
    data = f.read()

pattern = r'[^XYZ. ][^XYZ.]*\.'
matches = [match.group() for match in re.finditer(pattern, data)]

ans = max(matches, key=len)
print(len(ans))