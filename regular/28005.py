import re
with open('24_28005.txt') as f:
    data = f.readline()

pattern = r"([^@.]*[.])+([^@.])*\@((gmail.com)|(yandex.ru))"

matches = [match.group() for match in re.finditer(pattern, data)]
print(matches)
answer = max(matches, key=len)
print(len(answer))