from collections import deque


MAX = 100001
N, K = map(int, input().split())
visited = [0] * MAX
visited[N] = 1
dq = deque()
dq.append(N)

while dq:
    now = dq.popleft()
    next1, next2, next3 = now - 1, now + 1, 2 * now
    if 0 <= next1 < MAX and not visited[next1]:
        visited[next1] = visited[now] + 1
        dq.append(next1)
    if 0 <= next2 < MAX and not visited[next2]:
        visited[next2] = visited[now] + 1
        dq.append(next2)
    if 0 <= next3 < MAX and not visited[next3]:
        visited[next3] = visited[now] + 1
        dq.append(next3)

print(visited[K] - 1)
