num = list(map(int, input().split()))
p1, c1, p2, c2 = num[0], num[1], num[2], num[3]
g1 = p1 * c1
g2 = p2 * c2

if g1 == g2:
    print(0)
elif g1 < g2:
    print(1)
else:
    print(-1)