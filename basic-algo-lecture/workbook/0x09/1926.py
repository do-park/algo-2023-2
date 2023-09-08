# O l1: 그림의 개수 / l2: 가장 넓은 그림의 넓이
# I N:도화지의 세로 크기 / M: 도화지의 가로 크기 / P: 그림의 정보
# 그림: 1로 가로나 세로로 연결된 것, 그림의 넓이: 그림에 포함된 1의 개수

from collections import deque


ds = [[0, -1], [0, 1], [-1, 0], [1, 0]]

N, M = map(int, input().split())
P = list(list(map(int, input().split())) for _ in range(N))
visited = [[0] * M for _ in range(N)]
dq = deque()
result1, result2 = 0, 0

for n in range(N):
    for m in range(M):
        if P[n][m] == 1 and not visited[n][m]:
            visited[n][m] = 1
            dq.append([n, m])
            result1 += 1
            size = 1
            while dq:
                y, x = dq.pop()
                for d in range(4):
                    dy, dx = ds[d]
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and P[ny][nx] == 1 and not visited[ny][nx]:
                        visited[ny][nx] = 1
                        dq.append([ny, nx])
                        size += 1
            result2 = max(result2, size)

print(result1)
print(result2)