V, N = map(int, input().split())
total = V * N

for i in range(10, 100, 10):
    if i < 90:
        if (i*total) % 100 == 0:
            print(int((i*total) / 100), end=" ")
        else:
            print(int((i * total) / 100 + 1), end=" ")
    else:
        if (i * total) % 100 == 0:
            print(int((i * total) / 100))
        else:
            print(int((i * total) / 100 + 1))