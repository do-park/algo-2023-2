I = [0] * 9
for i in range(9):
    I[i] = int(input())
print(max(I))
print(I.index(max(I)) + 1)