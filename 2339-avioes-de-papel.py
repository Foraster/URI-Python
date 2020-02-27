num = list(map(int, input().split()))
if num[2] * num[0] <= num[1]:
    print('S')
else:
    print('N')