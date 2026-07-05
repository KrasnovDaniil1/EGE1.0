data = "6 72 8 166 2 5"
l = 0
m = 0
for r in range(len(data) - 1):
    if int(data[r]) < int(data[r + 1]):
        l = r + 1
    length = r - l + 2
    m = max(m, length)
# print(m)

l = 3
m = 0

r = 3
length = 3

m = 3
