SUM, MIN = 0, 1e9
for i in range(7):
    I = int(input())
    if I % 2 == 1:
        SUM += I
        if MIN > I:
            MIN = I

if SUM == 0:
    print(-1)
else:
    print(SUM)
    print(MIN)