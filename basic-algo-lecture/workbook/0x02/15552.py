import sys

T = int(sys.stdin.readline())
for t in range(T):
    I = list(map(int, sys.stdin.readline().split()))
    print(sum(I))