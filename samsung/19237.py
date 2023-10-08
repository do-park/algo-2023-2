# RESULT: 1번 상어만 남게 되기까지 몇 초가 걸리는지

N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
shark_poses = [[-1, -1] for _ in range(M)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            shark_poses[matrix[i][j] - 1] = [i, j]

shark_dists = list(map(int, input().split()))
for m in range(M):
    shark_dists[m] -= 1

shark_move_priority = [[[] for _ in range(4)] for __ in range(M)]
for m in range(M):
    for d in range(4):
        inputs = list(map(int, input().split()))
        shark_move_priority[m][d] = [inputs[0] - 1, inputs[1] - 1, inputs[2] - 1, inputs[3] - 1]

dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[[-1, -1] for _ in range(N)] for __ in range(N)]
RESULT = 0

while True:
    # 1. 모든 상어가 자신의 위치에 냄새를 뿌린다.
    for idx in range(M):
        if shark_poses[idx] != [-1, -1]:
            y, x = shark_poses[idx]
            visited[y][x] = [idx, K]

    # 2. 모든 상어가 동시에 상하좌우 인접한 칸 중 하나로 이동한다.
    # - 인접한 칸 중 아무 냄새도 없는 칸
    # - 자신의 냄새가 있는 칸
    # - 두 조건을 만족하는 칸이 여러개라면 각 상어의 우선순위에 따라 이동

    # 3. 이동 후 한 칸에 여러 마리의 상어가 있으면, 가장 작은 번호의 상어만 남고 나머지는 쫓겨난다

    next_shark_poses = [[-1, -1] for _ in range(M)]

    for idx in range(M):
        if shark_poses[idx] == [-1, -1]:
            continue
        y, x = shark_poses[idx]
        for d in shark_move_priority[idx][shark_dists[idx]]:
            ny, nx = y + dys[d], x + dxs[d]
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == [-1, -1]:
                next_shark_poses[idx], shark_dists[idx] = [ny, nx], d
                break
        if next_shark_poses[idx] == [-1, -1]:
            for d in shark_move_priority[idx][shark_dists[idx]]:
                ny, nx = y + dys[d], x + dxs[d]
                if 0 <= ny < N and 0 <= nx < N and visited[ny][nx][0] == idx:
                    next_shark_poses[idx], shark_dists[idx] = [ny, nx], d
                    break

        if next_shark_poses.count(next_shark_poses[idx]) > 1:
            next_shark_poses[idx] = [-1, -1]

    shark_poses = next_shark_poses
    RESULT += 1

    for i in range(N):
        for j in range(N):
            if visited[i][j] != [-1, -1]:
                idx, k = visited[i][j]
                if k == 1:
                    visited[i][j] = [-1, -1]
                else:
                    visited[i][j] = [idx, k-1]

    if shark_poses.count([-1, -1]) == M - 1:
        break

    if RESULT >= 1000:
        RESULT = -1
        break

print(RESULT)