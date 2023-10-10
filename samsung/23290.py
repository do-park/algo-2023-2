# 예제 5, 8 통과 X

import copy


# RESULT: 연습을 모두 마쳤을 때, 격자에 있는 물고기의 수
N = 4
M, S = map(int, input().split())
fishes_input = [tuple(map(int, input().split())) for _ in range(M)]
sy, sx = map(int, input().split())

# empty_fish_list = [0 for _ in range(8)]
fishes = [[[0 for _ in range(8)] for _ in range(N)] for __ in range(N)] # 물고기

for m in range(M):
    fy, fx, fd = fishes_input[m]
    fishes[fy-1][fx-1][fd-1] += 1
sy, sx = sy-1, sx-1

dists = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
visited = [[0 for _ in range(N)] for __ in range(N)] # 물고기 냄새

def move(shark_y, shark_x, depth, cnt, arr):
    global max_eat_fishes, shark_trace, sy, sx
    if depth == 0:
        if cnt >= max_eat_fishes:
            max_eat_fishes = cnt
            shark_trace = copy.deepcopy(arr)
            sy, sx = shark_y, shark_x
        return
    for (sdy, sdx) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ny, nx = shark_y + sdy, shark_x + sdx
        if 0 <= ny < N and 0 <= nx < N:
            temp = moved_fishes[ny][nx]
            if sum(temp):
                moved_fishes[ny][nx] = [0 for _ in range(8)]
                move(ny, nx, depth-1, cnt + sum(temp), arr+[(ny, nx)])
            else:
                move(ny, nx, depth-1, cnt, arr)
            moved_fishes[ny][nx] = temp

for s in range(S):
    # 1. 모든 물고기에게 복제 마법을 시전한다. 5번에서 물고기가 복제되어 칸에 나타난다.
    moved_fishes = [[[0 for _ in range(8)] for _ in range(N)] for __ in range(N)]

    # 2. 모든 물고기가 한 칸 이동한다. 상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없다.
    # -- 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전
    # -- 이동할 수 있는 칸이 없으면 이동을 하지 않는다
    for y in range(N):
        for x in range(N):
            for idx in range(8):
                if fishes[y][x][idx]:
                    for d in range(8):
                        nd = (idx - d) % 8
                        ndy, ndx = dists[nd]
                        ny, nx = y + ndy, x + ndx
                        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and (ny, nx) != (sy, sx):
                            moved_fishes[ny][nx][nd] = fishes[y][x][idx]
                            break
                    else:
                        moved_fishes[y][x][idx] = fishes[y][x][idx]

    # 4. 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다
    for y in range(N):
        for x in range(N):
            if visited[y][x]:
                visited[y][x] = visited[y][x] - 1

    # 3. 상어가 연속해서 3칸 이동한다.
    # -- 상하좌우로 인접한 칸으로 이동할 수 있으며, 격자를 벗어날 수 없다
    # -- 연속해서 이동하는 중에 상어가 물고기가 있는 칸으로 이동하게 되면 그 칸의 물고기는 격자에서 제외되며 물고기 냄새를 남긴다
    # -- 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며, 그러한 방법이 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용한다
    # -- 사전 순으로 앞서기: 상1 좌2 하3 우4 -> 수를 이어붙여 하나의 정수로 만들어 숫자가 작을수록 사전 순으로 앞선다
    max_eat_fishes = 0
    shark_trace = []
    move(sy, sx, 3, 0, [])
    for (y, x) in shark_trace:
        visited[y][x] = 2
        moved_fishes[y][x] = [0 for _ in range(8)]

    # 5. 1에서 사용한 복제 마법이 완료된다. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다
    for y in range(N):
        for x in range(N):
            for idx in range(8):
                fishes[y][x][idx] += moved_fishes[y][x][idx]

    for f in fishes:
        print(f)

    for v in visited:
        print(v)

    print(sy, sx)

    print(shark_trace)

# RESULT: 연습을 모두 마쳤을 때, 격자에 있는 물고기의 수
RESULT = 0
for y in range(N):
    for x in range(N):
        RESULT += sum(fishes[y][x])
print(RESULT)