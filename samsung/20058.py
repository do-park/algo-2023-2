# RESULT1: 남아있는 얼음 A[r][c]의 합
# RESULT2: 가장 큰 덩어리가 차지하는 칸의 개수
from collections import deque


N, Q = map(int, input().split())
W = 2 ** N
A = [list(map(int, input().split())) for _ in range(W)]
L = list(map(int, input().split()))


for l in L:
    # 1. 격자를 (2 ** L) * (2 ** L) 크기의 부분 격자로 나눈다
    # 2. 모든 격자를 시계 방향으로 90도 회전시킨다.
    w = 2 ** l
    sub_w = W // w
    NA = [[0] * W for _ in range(W)]

    for i in range(0, W, w):
        for j in range(0, W, w):
            for y in range(w):
                for x in range(w):
                    NA[i + y][j + x] = A[i + w - 1- x][j + y]

    # 3. 얼음이 있는 칸 3개 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
    temp = [[0] * W for _ in range(W)]
    for y in range(W):
        for x in range(W):
            if NA[y][x] > 0:
                ice = 0
                for (dy, dx) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < W and 0 <= nx < W and NA[ny][nx] > 0:
                        ice += 1
                temp[y][x] = NA[y][x] if ice >= 3 else NA[y][x] - 1
    A = temp

# RESULT1: 남아있는 얼음 A[r][c]의 합
RESULT1 = 0
for s in A:
    RESULT1 += sum(s)
print(RESULT1)


# RESULT2: 가장 큰 덩어리가 차지하는 칸의 개수
RESULT2 = 0
Q = deque()
visited = [[0] * W for _ in range(W)]
for y in range(W):
    for x in range(W):
        if A[y][x] > 0 and not visited[y][x]:
            ice_size = 1
            Q.append((y, x))
            visited[y][x] = 1
            while Q:
                r, c = Q.popleft()
                for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < W and 0 <= nc < W and A[nr][nc] > 0 and not visited[nr][nc]:
                        ice_size += 1
                        Q.append((nr, nc))
                        visited[nr][nc] = 1
            RESULT2 = max(RESULT2, ice_size)
print(RESULT2)