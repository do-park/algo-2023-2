# 영식 30초마다 10원 / 민식 60초마다 15원

N = int(input())
I = list(map(int, input().split()))

Y, M = 0, 0
for i in I:
    Y += ((i // 30) + 1) * 10
    M += ((i // 60) + 1) * 15

if Y > M:
    print('M', M)
elif Y < M:
    print('Y', Y)
else:
    print('Y M', Y)