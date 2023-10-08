from collections import deque


T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())
    MAT = [[0] * M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        MAT[r][c] = 1

    RESULT = 0
    dq = deque()
    visited = [[0] * M for _ in range(N)]
    for n in range(N):
        for m in range(M):
            if MAT[n][m] and not visited[n][m]:
                RESULT += 1
                visited[n][m] = 1
                dq.append([n, m])
                while dq:
                    y, x = dq.popleft()
                    for (dy, dx) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < M and MAT[ny][nx] and not visited[ny][nx]:
                            visited[ny][nx] = 1
                            dq.append([ny, nx])
    print(RESULT)