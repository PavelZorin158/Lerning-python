file_date = open('data_input.txt', 'r')
data_input = [line for line in file_date]
file_date.close()
for n in range(len(data_input)):
    data_input[n] = data_input[n].replace('\n', '')

fx = [] # координаты Х всех ферзей
fy = [] # координаты Y всех ферзей
res = 'NO'
f = [[0] * 8 for i in range(8)]

for i in range(8):
    s = data_input[i].split()
    x = int(s[0])
    y = int(s[1])
    fx.append(x-1)
    fy.append(y-1)
    f[x-1][y-1] = 1

# проверяем есть ли несколько ферзей с одинаковой координатой X
for x in range(1, 9):
    if fx.count(x) > 1:
        res = 'YES'

# проверяем есть ли несколько ферзей с одинаковой координатой Y
for y in range(1, 9):
    if fy.count(y) > 1:
        res = 'YES'

for i in range(8):
    n = 0
    x = fx[i]
    y = fy[i]
    y1 = fy[i]
    for x1 in range(x+1,8): # ищем X+1, Y+1
        if y1 < 7:
            y1 += 1
            if f[x1][y1] == 1:
                res = 'YES'
    y1 = fy[i]
    for x1 in range(x+1,8): # ищем X+1, Y-1
        if y1 > 0:
            y1 -= 1
            if f[x1][y1] == 1:
                res = 'YES'
    y1 = fy[i]
    for x1 in range(x-1,-1,-1): # ищем X-1, Y-1
        if y1 > 0:
            y1 -= 1
            if f[x1][y1] == 1:
                res = 'YES'
    y1 = fy[i]
    for x1 in range(x-1,-1,-1): # ищем X-1, Y+1
        if y1 < 7:
            y1 += 1
            if f[x1][y1] == 1:
                res = 'YES'
            
for y in range(7,-1,-1):
    for x in range(8):
        print(f[x][y], end='  ')
    print()
print(res)
