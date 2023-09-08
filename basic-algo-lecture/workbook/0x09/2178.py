# INPUT l1: 두 정수 N(세로), M(가로) / l2~: 미로
# OUTPUT: (1, 1) ~ (N, M)까지 지나야 하는 최소의 칸 수
# 1은 이동 가능, 0은 이동 불가

from collections import deque


ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]

N, M = map(int, input().split())
MAZE = [list(map(int, input())) for _ in range(N)]
dq = deque()
visited = [[0] * M for _ in range(N)]

visited[0][0] = 1
dq.append([0, 0])
while dq:
    y, x = dq.popleft()
    for d in range(4):
        dy, dx = ds[d]
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and MAZE[ny][nx] and not visited[ny][nx]:
            visited[ny][nx] = visited[y][x] + 1
            dq.append([ny, nx])

print(visited[N-1][M-1])