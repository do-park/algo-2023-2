for tc in range(3):
    I = list(map(int, input().split()))
    front = I.count(0)
    if front == 0:
        print('E')
    elif front == 1:
        print('A')
    elif front == 2:
        print('B')
    elif front == 3:
        print('C')
    else:
        print('D')