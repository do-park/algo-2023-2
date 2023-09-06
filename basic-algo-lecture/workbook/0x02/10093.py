I = list(map(int, input().split()))
I.sort()
I[0] += 1
print(max(0, I[1] - I[0]))
for i in range(I[0], I[1]):
    print(i, end=" ")