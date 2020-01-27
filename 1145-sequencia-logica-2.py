num = list(map(int, input().split()))
x, y = num[0], num[1]

for i in range(1, y+1):
    if i % x == 0:
        print(i)
    else:
        print(i, end=" ")
