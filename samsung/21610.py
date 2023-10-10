# RESULT: M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
spells = [list(map(int, input().split())) for _ in range(M)]

dists = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

# (N-1, 0) (N-1, 1) (N-2, 0) (N-2, 1)에 비구름이 생긴다
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]


# 구름에 이동을 M번 명령한다.
for spell in spells:
    d, s = spell[0] - 1, spell[1]
    # 1. 모든 구름이 d 방향으로 s칸 이동한다
    # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.

    for i in range(len(clouds)):
        y, x = clouds[i]
        ny, nx = (y + dists[d][0] * s) % N, (x + dists[d][1] * s) % N
        clouds[i] = (ny, nx)
        A[ny][nx] += 1

    # 3. 구름이 모두 사라진다.

    # 4. 2에서 물이 증가한 칸 (r, c)의 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물의 양이 증가한다.
    # -- 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다. (진짜 인접한 칸만)
    for (r, c) in clouds:
        cnt = 0
        for (dr, dc) in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and A[nr][nc] > 0:
                cnt += 1
        A[r][c] += cnt

    # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    next_cloud = []
    for i in range(N):
        for j in range(N):
            if A[i][j] > 1 and (i, j) not in clouds:
                next_cloud.append((i, j))
                A[i][j] -= 2

    clouds = next_cloud

# 이동이 끝난 후 바구니에 들어있는 물의 양의 합을 출력한다
RESULT = 0
for a in A:
    RESULT += sum(a)
print(RESULT)