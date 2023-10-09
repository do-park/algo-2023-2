# RESULT: 토네이도가 소멸되었을 때 격자 밖으로 나간 모래의 양

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 토네이도를 시전하면 격자의 가운데 칸부터 토네이도의 이동이 시작된다. 토네이도는 한 번에 한 칸 이동한다.
# 토네이도가 한 칸 이동할 때마다 모래는 일정한 비율로 흩날리게 된다.
# 소수점 이하는 버린다
# 토네이도는 (0, 0)까지 이동한 뒤 소멸한다

RESULT = 0
y, x = N // 2, N // 2
d = -1
   
# [y축, x축, 비율]
XP = [
    [-2, 0, 0.02],
    [-1, -1, 0.01], [-1, 0, 0.07], [-1, 1, 0.10],
    [0, 2, 0.05],
    [1, -1, 0.01], [1, 0, 0.07], [1, 1, 0.10],
    [2, 0, 0.02]
]
# ny = y + X[n][0], nx = x + X[n][1] * d

YP = [
    [-1, -1, 0.01], [-1, 1, 0.01],
    [0, -2, 0.02], [0, -1, 0.07], [0, 1, 0.07], [0, 2, 0.02],
    [1, -1, 0.10], [1, 1, 0.10],
    [2, 0, 0.05]
]
# ny = y + Y[n][0] * d, nx = x + Y[n][1]

for i in range(1, N + 1):
    for j in range(i):
        x = x + d
        left_sand = matrix[y][x]
        # 모래 날리기
        for [r, c, p] in XP:
            ny = y + r
            nx = x + c * d
            sand = int(matrix[y][x] * p)
            if 0 <= ny < N and 0 <= nx < N:
                matrix[ny][nx] += sand
            else:
                RESULT += sand
            left_sand -= sand

        nx = x + d
        if 0 <= nx < N and 0 <= y < N:
            matrix[y][nx] += left_sand
        else:
            RESULT += left_sand
        matrix[y][x] = 0

        if y <= 0 and x <= 0:
            break

    if y <= 0 and x <= 0:
        break

    d *= -1

    for j in range(i):
        y = y + d
        left_sand = matrix[y][x]
        # 모래 날리기
        for [r, c, p] in YP:
            ny = y + r * d
            nx = x + c
            sand = int(matrix[y][x] * p)
            if 0 <= ny < N and 0 <= nx < N:
                matrix[ny][nx] += sand
            else:
                RESULT += sand
            left_sand -= sand

        ny = y + d
        if 0 <= x < N and 0 <= ny < N:
            matrix[ny][x] += left_sand
        else:
            RESULT += left_sand
        matrix[y][x] = 0

print(RESULT)