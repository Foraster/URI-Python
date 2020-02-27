num = list(map(int, input().split()))

if (num[0] == 0 and num[1] == 0) or (num[0] == 0 and num[1] == 1):
    print('C')
elif num[0] == 1 and num[1] == 0:
    print('B')
else:
    print('A')
