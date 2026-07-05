ans = []
for N in range (100000, 1, -1):
    R = bin(N)[2:]
    if N %3 == 0:
        R = R + R[-3:]
    else:
        R = R + bin(N % 3 * 3)[2:]
    R = int(R, 2)
    if R <= 170:
        ans.append(R)

print(max(ans))
# print('166')