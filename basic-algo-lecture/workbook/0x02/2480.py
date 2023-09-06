# 1 ~ 6 눈 가진 3개의 주사위 던져서
# 같은 눈이 3개가 나오면 10000 + 같은눈 * 1000
# 같은 눈이 2개가 나오면 1000원 + 같은눈 * 100
# 모두 다른 눈 가장 큰눈 * 100
# INPUT: 3개 주사위의 눈
# OUTPUT: 상금

numbers = [0]*10
V = list(map(int, input().split()))

for v in V:
    numbers[v] += 1

max_cnt = max(numbers)

if max_cnt == 3:
    print(10000 + numbers.index(max_cnt) * 1000)
elif max_cnt == 2:
    print(1000 + numbers.index(max_cnt) * 100)
else:
    print(max(V) * 100)