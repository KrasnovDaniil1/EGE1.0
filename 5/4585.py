def f(n):
    n = bin(n)[2:]
    if n.count('1') %2 == 0:
        n += '0'
        n = '10' + n[2:]
    else:
        n += '1'
        n = '11' + n[2:]
    return int(n, 2)

i = 0
while True:
    if f(i) >= 16:
        print(i)
        break
    i+=1