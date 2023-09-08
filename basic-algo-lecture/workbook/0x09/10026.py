from collections import deque


N = int(input())
PICTURE = [list(map(str, input())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
dq = deque()

result1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = 1
            dq.append([i, j])
            color = PICTURE[i][j]
            result1 += 1
            while dq:
                y, x = dq.popleft()
                for (dy, dx) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < N and PICTURE[ny][nx] == color and not visited[ny][nx]:
                        visited[ny][nx] = 1
                        dq.append([ny, nx])
print(result1, end=" ")

visited = [[0] * N for _ in range(N)]

# 빨간색과 녹색은 같은 색으로 처리 (R, G) 파란색만 따로 처리 (B)
result2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = 1
            dq.append([i, j])
            color = PICTURE[i][j]
            result2 += 1
            while dq:
                y, x = dq.popleft()
                for (dy, dx) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                        if (PICTURE[ny][nx] != 'B' and color != 'B') or (PICTURE[ny][nx] == 'B' and color == 'B'):
                            visited[ny][nx] = 1
                            dq.append([ny, nx])
print(result2)