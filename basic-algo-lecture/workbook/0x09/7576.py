# O: 토마토가 모두 익을 때까지 최소 날짜 / 처음부터 다 익어 있었으면 0 / 모두 익지 못하는 상황이면 -1
# I: M 가로 N 세로 / 토마토 정보

from collections import deque


ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
M, N = map(int, input().split())
TOMATOES = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dq = deque()
done, empty = 0, 0

for n in range(N):
    for m in range(M):
        if TOMATOES[n][m] == 1:
            visited[n][m] = 1
            dq.append([n, m])
            done += 1
        elif TOMATOES[n][m] == -1:
            empty += 1

while dq:
    y, x = dq.popleft()
    for d in range(4):
        dy, dx = ds[d]
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and TOMATOES[ny][nx] == 0 and not visited[ny][nx]:
            visited[ny][nx] = visited[y][x] + 1
            dq.append([ny, nx])
            done += 1

result = 0
total = M * N
if done + empty == total:
    for v in visited:
        result = max(result, max(v))
    print(result - 1)
elif done + empty < total:
    print(-1)