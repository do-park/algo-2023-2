from collections import deque


N, M, K = map(int, input().split()) # N * M 격자, K번의 액션
powers = [list(map(int, input().split())) for _ in range(N)] # 포탑의 공격력 (부서진 포탑 0)
attacking_phase = [[0 for _ in range(M)] for __ in range(N)] # 언제 공격했는지 (숫자가 클수록 최근에 공격함)

razer_dists = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우선순위: 우하좌상
bomb_dists = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

score = N + M
# print(score)

for k in range(1, K+1):
    # print('# phase ', k)

    # 공격자와 방어자 선정
    # ---- 가장 약한 포탑 (공격자)
    # ------ 1. 공격력이 가장 낮은 포탑
    # ------ 2. 같은 조건이라면, 공격력이 가장 낮은 포탑이 2개 이상이라면 가장 최근에 공격한 포탑
    # ------ 3. 같은 조건이라면, 행과 열의 합이 가장 큰 포탑 (공)
    # ------ 4. 같은 조건이라면, 각 포탑 위치의 열 값이 가장 큰 포탑
    # ---- 가장 강한 포탑
    # ------ 1. 공격력이 가장 높은 포탑
    # ------ 2. 같은 조건이라면, 공격한지 가장 오래된 포탑이 가장 강한 포탑
    # ------ 3. 같은 조건이라면, 행과 열의 합이 가장 작은 포탑 (방)
    # ------ 4. 같은 조건이라면, 각 포탑 위치의 열 값이 가장 작은 포탑

    # 1
    min_power, max_power = 5001, 0
    attackers_pos = [] # 공격자
    defencers_pos = [] # 방어자

    for i in range(N):
        for j in range(M):
            if not powers[i][j]:
                continue
            if powers[i][j] < min_power:
                min_power = powers[i][j]
                attackers_pos = [(i, j)]
            elif powers[i][j] == min_power:
                attackers_pos.append((i, j))
            if powers[i][j] > max_power:
                max_power = powers[i][j]
                defencers_pos = [(i, j)]
            elif powers[i][j] == max_power:
                defencers_pos.append((i, j))

    # print('# 0-1')
    # print('attackers', attackers_pos)
    # print('defencers', defencers_pos)

    # 2
    attackers_attacking_phase = []
    defencers_attacking_phase = []

    for (i, j) in attackers_pos:
        attackers_attacking_phase.append(attacking_phase[i][j])

    for (i, j) in defencers_pos:
        defencers_attacking_phase.append(attacking_phase[i][j])

    max_phase, min_phase = 0, K+1
    temp_attackers_pos = [] # 공격자
    temp_defencers_pos = [] # 방어자

    for i in range(len(attackers_attacking_phase)):
        if attackers_attacking_phase[i] > max_phase:
            max_phase = attackers_attacking_phase[i]
            temp_attackers_pos = [(attackers_pos[i])]
        elif attackers_attacking_phase[i] == max_phase:
            temp_attackers_pos.append((attackers_pos[i]))

    for i in range(len(defencers_attacking_phase)):
        if defencers_attacking_phase[i] < min_phase:
            min_phase = defencers_attacking_phase[i]
            temp_defencers_pos = [defencers_pos[i]]
        elif defencers_attacking_phase[i] == min_phase:
            temp_defencers_pos.append((defencers_pos[i]))

    # print('# 0-2')
    # print('attackers', temp_attackers_pos)
    # print('defencers', temp_defencers_pos)

    # 3
    # ------ 3. 같은 조건이라면, 행과 열의 합이 가장 큰 포탑 (공)
    # ------ 3. 같은 조건이라면, 행과 열의 합이 가장 작은 포탑 (방)
    total_a, total_d = 0, 21
    total_attackers_pos = []
    total_defencers_pos = []

    for (i, j) in temp_attackers_pos:
        if total_a < i + j:
            total_a = i + j
            total_attackers_pos = [(i, j)]
        elif total_a == i + j:
            total_attackers_pos.append((i, j))

    for (i, j) in temp_defencers_pos:
        if total_d > i + j:
            total_d = i + j
            total_defencers_pos = [(i, j)]
        elif total_d == i + j:
            total_defencers_pos.append((i, j))

    # 4
    a, d = -1, 11
    attacker, defencer = (-1, -1), (-1, -1) # 열 값이 가장 큰 포탑이 약한 / 열 값이 가장 작은 포탑이 강한
    for (i, j) in total_attackers_pos:
        if a < j:
            a = j
            attacker = (i, j)

    for (i, j) in total_defencers_pos:
        if d > j:
            d = j
            defencer = (i, j)

    if attacker == defencer:
        break

    # print('# 0-4')
    # print('attacker: ', attacker)
    # print('defencer', defencer)

    # 1. 공격자 선정
    # -- 부서지지 않은 포탑 중 가장 약한 포탑의 공격력이 N + M 만큼 증가
    ay, ax = attacker
    powers[ay][ax] += score
    attacking_phase[ay][ax] = k
    power = powers[ay][ax]
    half_power = power // 2

    # 2. 공격자의 공격
    # -- 자신을 제외한 가장 강한 포탑을 공격
    # 2-1. 레이저 공격
    # ---- 0 ~ N-1, 0 ~ M-1이 연결된 상하좌우로 이동 가능한 BFS, 단 부서진 포탑이 있는 위치는 지날 수 없다
    # ---- 우하좌상의 우선순위대로 먼저 움직인 경로가 선택
    # ---- 최단 경로가 정해졌으면, 공격 대상은 공격자의 공격력 피해만큼의 피해를 입히며, 피해를 입은 포탑은 해당 수치만큼 공격력이 줄어든다.
    # ---- 공격 대상을 제외한 레이저 경로에 있는 포탑도 공격을 받는데, 공격자의 공격력 // 2만큼의 피해를 입는다.
    Q = deque()
    Q.append((ay, ax))
    visited = [[[] for _ in range(M)] for __ in range(N)]

    visited[ay][ax] = [(ay, ax)]
    while Q:
        y, x = Q.popleft()
        for (ddy, ddx) in razer_dists:
            ny, nx = (y + ddy) % N, (x + ddx) % M
            if powers[ny][nx] > 0 and len(visited[ny][nx]) == 0:
                Q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + [(ny, nx)]

    dy, dx = defencer
    route = visited[dy][dx]
    not_attacked_tower = [[True for _ in range(M)] for __ in range(N)]
    not_attacked_tower[ay][ax] = False

    if len(route) != 0:
        for i in range(1, len(route)-1):
            y, x = route[i]
            powers[y][x] = max(0, powers[y][x] - half_power)
            not_attacked_tower[y][x] = False
        powers[dy][dx] = max(0, powers[dy][dx] - power)
        not_attacked_tower[dy][dx] = False

        # print('# 2-1')
        # for i in powers:
        #     print(i)

    else:
        # 2-2. 포탄 공격
        # ---- 공격 대산에 포탄을 던져, 공격 대상은 공격자 공격력 만큼의 피해를 받고, 주위 8개의 방향에 있는 포탑은 공격자 공격력 // 2 만큼의 피해를 받는다
        # ---- 공격자 포탑은 해당 공격에 영향을 받지 않는다
        # ---- 0 ~ N-1, 0 ~ M-1이 연결된 식으로 공격을 받는다
        powers[dy][dx] = max(0, powers[dy][dx] - power)
        not_attacked_tower[dy][dx] = False
        for (ddy, ddx) in bomb_dists:
            ny, nx = (dy + ddy) % N, (dx + ddx) % M
            if (ny, nx) != (ay, ax) and powers[ny][nx] != 0:
                powers[ny][nx] = max(0, powers[ny][nx] - half_power)
                not_attacked_tower[ny][nx] = False

        # print('# 2-2')
        # for i in powers:
        #     print(i)

    # 3. 포탑 부서짐
    # -- 공격을 받아 공격력이 0 이해가 된 포탑은 부서진다

    # 4. 포탑 정비
    # -- 공격이 끝났으면, 부서지지 않은 포탑 중 공격과 무관했던 포탑은 공격력이 1씩 올라간다. (공격자도 아니고, 공격에 피해를 입은 포탑도 아니다)
    for i in range(N):
        for j in range(M):
            if not_attacked_tower[i][j] and powers[i][j] > 0:
                powers[i][j] += 1
    # print('# 4')
    # for i in powers:
    #     print(i)
    #
    # print()

# RESULT: 전체 과정이 종료된 후 남아있는 포탑 중 가장 강한 포탑의 공격력을 출력
RESULT = 0
for p in powers:
    RESULT = max(RESULT, max(p))
print(RESULT)