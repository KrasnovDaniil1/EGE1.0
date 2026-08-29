import re

with open(r"./8835.txt") as f:
    data = f.read()

pattern = r'[^ .][^.]+\.'
matches = [match.group() for match in re.finditer(pattern, data)]

ans = 0
for match in matches:
    cnt_M = match.count('M')
    if cnt_M == 112:
        ans = max(ans, len(match))
    elif cnt_M > 112 and len(match) > ans:
        r = 0
        while match[r:].count("M") > 112:
            r += 1
        ans = max(ans, len(match[r:]))

print(ans)

# [  3,   9,  12,  17, 21]
# ***M****M***M****M***M****.

# 1M -> [pos_M[-2] + 1:]
# 2M -> [pos_M[-3] + 1:]
# 112M -> [pos_M[-113] + 1:]