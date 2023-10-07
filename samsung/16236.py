# 9:00

# O: 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지

from collections import deque


N = int(input())
ocean = [list(map(int, input().split())) for _ in range(N)]

shark_pos, shark_size, shark_exp = [0, 0], 2, 0
result = 0

for i in range(N):
    for j in range(N):
        if ocean[i][j] == 9:
            shark_pos = [i, j]
            ocean[i][j] = 0

dys = [-1, 0, 1, 0]
dxs = [0, -1, 0, 1]

X, Y = 1, 0

while True:
    # BFS 돌려서 물고기 거리 구한다
    Q = deque()
    visited = [[0] * N for _ in range(N)]

    Q.append(shark_pos)
    visited[shark_pos[Y]][shark_pos[X]] = 1

    while Q:
        y, x = Q.popleft()
        for d in range(4):
            ny, nx = y + dys[d], x + dxs[d]
            if 0 <= ny < N and 0 <= nx < N and ocean[ny][nx] <= shark_size and not visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                Q.append([ny, nx])

    # 먹을 물고기를 고른다 (칸의 개수가 최소, 칸의 개수가 최소인 물고기가 많다면 가장 위, 가장 왼쪽)
    max_dinner_distance = 987654321
    dinner_pos, dinner_distance = [0, 0], max_dinner_distance

    for i in range(N):
        for j in range(N):
            if 0 < ocean[i][j] < shark_size and 0 < visited[i][j] < dinner_distance:
                dinner_pos = [i, j]
                dinner_distance = visited[i][j]

    # 가장 가까운 거리의 물고기를 먹는다 (해당 위치로 이동, exp+=1, exp == size 일 때 size+=1, exp = 0, 거리만큼 result+=1)
    # 가장 가까운 거리의 물고기가 없으면 종료하고 결과를 출력한다
    if dinner_distance == max_dinner_distance:
        break

    shark_pos = dinner_pos
    shark_exp += 1
    if shark_exp == shark_size:
        shark_size += 1
        shark_exp = 0
    result += dinner_distance - 1
    ocean[dinner_pos[Y]][dinner_pos[X]] = 0

print(result)