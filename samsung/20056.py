# RESULT: 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합

N, M, K = map(int, input().split())
fireballs = [list(map(int, input().split())) for _ in range(M)] # r, c, m, s, d (행, 렬, 질량, 속도, 방향)

for m in range(M):
    fireballs[m] = [fireballs[m][0] - 1, fireballs[m][1] - 1, fireballs[m][2], fireballs[m][3], fireballs[m][4]]

drs = [-1, -1, 0, 1, 1, 1, 0, -1]
dcs = [0, 1, 1, 1, 0, -1, -1, -1]

for k in range(K):
    matrix = [[[] for _ in range(N)] for __ in range(N)]

    # 1. 모든 파이어볼이 자신의 방향 d로 속력 s칸 만큼 이동한다.
    for idx in range(len(fireballs)):
        r, c, m, s, d = fireballs[idx]
        fireballs[idx][0] = (r + drs[d] * s) % N
        fireballs[idx][1] = (c + dcs[d] * s) % N
        matrix[fireballs[idx][0]][fireballs[idx][1]].append(idx)

    # 2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는
    # - 1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
    # - 2. 파이어볼은 4개의 파이어볼로 나누어진다.
    # - 3. 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
    # -- 질량은 합쳐진 파이어볼의 질량의 합 // 5
    # -- 속력은 합쳐진 파이어볼의 속력의 합 // 파이어볼의 개수
    # -- 방향은 합쳐지는 파이어볼의 방향이 모두 홀수이거나 짝수이면 0, 2, 4, 6 / 아니면 1, 3, 5, 7
    # - 4. 질량이 0인 파이어볼은 소멸되어 없어진다.
    next_fireballs = []

    for i in range(N):
        for j in range(N):
            if len(matrix[i][j]) > 1:
                CNT = len(matrix[i][j])
                sum_m, sum_s, cnt = 0, 0, CNT
                for fb in range(len(matrix[i][j])):
                    r, c, m, s, d = fireballs[matrix[i][j][fb]]
                    sum_m += m
                    sum_s += s
                    if d % 2: # 홀수라면
                        cnt -= 1
                if sum_m // 5 == 0:
                    continue
                if cnt == 0 or cnt == CNT:
                    for nd in [0, 2, 4, 6]:
                        next_fireballs.append([i, j, sum_m // 5, sum_s // CNT, nd])
                else:
                    for nd in [1, 3, 5, 7]:
                        next_fireballs.append([i, j, sum_m // 5, sum_s // CNT, nd])
            elif len(matrix[i][j]) == 1:
                next_fireballs.append(fireballs[matrix[i][j][0]])

    fireballs = next_fireballs

RESULT = 0
for fb in fireballs:
    RESULT += fb[2]

print(RESULT)