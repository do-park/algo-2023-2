import copy


shark = 17
dists = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

matrix = [[], [], [], []]
pos = [(-1, -1) for _ in range(17)]
for i in range(4):
    inputs = list(map(int, input().split()))
    for j in range(4):
        matrix[i].append((inputs[2 * j], inputs[2 * j + 1] - 1))
        pos[inputs[2 * j]] = (i, j)

first_blood = matrix[0][0]
matrix[0][0] = (shark, first_blood[1])
pos[first_blood[0]] = (-1, -1)
shark_y, shark_x = 0, 0
RESULT = first_blood[0]


def move(m, p, sy, sx, answer):
    global RESULT
    # 물고기 번호가 작은 물고기부터 순서대로 이동
    # 빈 칸과 다른 물고기가 있는 칸으로 이동 가능 (서로의 위치 교체)
    # 상어가 있거나 공간의 경계를 넘으면 이동할 수 있는 칸을 향할 때까지 방향을 45도 회전
    # 이동할 수 있는 칸이 없으면 이동을 하지 않는다
    for idx in range(1, 17):
        y, x = p[idx]
        if (y, x) == (-1, -1):
            continue
        a, b = m[y][x]
        for d in range(8):
            nd = (b+d) % 8
            ny = y + dists[nd][0]
            nx = x + dists[nd][1]
            if 0 <= ny < 4 and 0 <= nx < 4 and m[ny][nx][0] != shark:
                if (-1, -1) == m[ny][nx]:
                    p[idx] = (ny, nx)
                    m[y][x], m[ny][nx] = (-1, -1), (a, nd)
                else:
                    p[idx], p[m[ny][nx][0]] = (ny, nx), (y, x)
                    m[y][x], m[ny][nx] = m[ny][nx], (a, nd)
                break
    # 상어가 방향에 있는 칸으로 이동
    # 한 번에 여러 칸을 이동할 수 있지만, 지나가는 칸에 있는 물고기는 먹지 않는다
    # 물고기가 없는 칸으로는 이동할 수 없고, 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어난다.
    a, b = m[sy][sx]
    dy, dx = dists[b]
    for d in range(1, 4):
        ny, nx = sy + dy * d, sx + dx * d
        if 0 <= ny < 4 and 0 <= nx < 4 and m[ny][nx] != (-1, -1):
            na, nb = m[ny][nx]
            p[na] = (-1, -1)
            m[sy][sx], m[ny][nx] = (-1, -1), (a, nb)
            sy, sx = ny, nx
            answer += na

            RESULT = max(RESULT, answer)
            cm, cp = copy.deepcopy(m), copy.deepcopy(p)
            move(cm, cp, sy, sx, answer)

            answer -= na
            sy, sx = ny - dy * d, nx - dx * d
            m[sy][sx], m[ny][nx] = (a, b), (na, nb)
            p[na] = (ny, nx)


move(matrix, pos, shark_y, shark_x, RESULT)
print(RESULT)