def func(arg):
    if arg % 4 != 0:
        return 0
    if arg % 100 != 0 or arg % 400 == 0:
        return 1
    return 0


Y = int(input())
print(func(Y))