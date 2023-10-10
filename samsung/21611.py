# RESULT: 1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)
from collections import deque


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
spells = [tuple(map(int, input().split())) for _ in range(M)]

dist = [(-1, 0), (1, 0), (0, -1), (0, 1)]
RESULT = [0, 0, 0, 0]

# 마법사 상어의 위치는 (N//2, N//2), 토네이도 모양의 벽
sy, sx = N//2, N//2
for (D, S) in spells:
    D -= 1

    # 1. d 방향으로 거리가 s이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬을 모두 파괴한다. 구슬이 파괴되면 그 칸은 빈 칸이 된다.
    for s in range(1, S + 1):
        dy, dx = dist[D]
        ny, nx = sy + dy * s, sx + dx * s
        if 0 <= ny < N and 0 <= nx < N and A[ny][nx]:
            A[ny][nx] = 0

    # 2. 앞에 빈 칸이 생기면 구슬은 그 빈 칸으로 이동한다. 더 이상 구슬이 이동하지 않을 때까지 반복된다.
    Q = deque()
    d = -1
    r, c = sy, sx
    for n in range(1, N + 1):
        # x축 이동
        for i in range(n):
            c += d
            if A[r][c]:
                Q.append(A[r][c])
            if (r, c) == (0, 0):
                break
        if (r, c) == (0, 0):
            break
        # y축 이동
        d *= -1
        for i in range(n):
            r += d
            if A[r][c]:
               Q.append(A[r][c])

    if not len(Q):
        continue

    # 3. 4개 이상 연속하는 구슬이 있을 때, 구슬이 폭발한다. 모든 구슬이 폭발한 뒤에 구슬이 다시 이동한다. 더 이상 구슬이 폭발하지 않을 때까지 반복된다.
    while True:
        cnt = 1
        for q in range(1, len(Q)):
            if Q[q] == Q[q-1]:
                cnt += 1
            else:
                if cnt >= 4:
                    RESULT[Q[q-1]] += cnt
                    for c in range(cnt):
                        Q[q-c-1] = 0
                cnt = 1
        if cnt >= 4:
            RESULT[Q[len(Q) - 1]] += cnt
            for c in range(cnt):
                Q[len(Q) - c - 1] = 0
        if Q.count(0) == 0:
            break
        tQ = deque()
        for q in range(len(Q)):
            if Q[q]:
                tQ.append(Q[q])
        Q = tQ

    if not len(Q):
        continue

    # 4. 연속하는 구슬을 하나의 그룹으로 묶고, 하나의 그룹을 두 개의 구슬로 변환한다. => (구슬의 개수, 구슬의 번호) 구슬이 칸 수보다 많으면 그 구슬은 사라진다.
    tQ = deque()
    cnt = 1
    for q in range(1, len(Q)):
        if Q[q] == Q[q-1]:
            cnt += 1
        else:
            tQ.append(cnt)
            tQ.append(Q[q-1])
            cnt = 1
    tQ.append(cnt)
    tQ.append(Q[len(Q)-1])

    A = [[0 for _ in range(N)] for _ in range(N)]
    d = -1
    r, c = sy, sx
    for n in range(1, N + 1):
        # x축 이동
        for i in range(n):
            c += d
            A[r][c] = tQ.popleft()
            if (r, c) == (0, 0) or len(tQ) == 0:
                break
        if (r, c) == (0, 0) or len(tQ) == 0:
            break
        # y축 이동
        d *= -1
        for i in range(n):
            r += d
            A[r][c] = tQ.popleft()
            if len(tQ) == 0:
                break
        if len(tQ) == 0:
            break

print(RESULT[1] * 1 + RESULT[2] * 2 + RESULT[3] * 3)