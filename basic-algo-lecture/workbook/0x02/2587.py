I = [0] * 5
for i in range(5):
    I[i] = int(input())
I.sort()
print(sum(I)//5)
print(I[2])