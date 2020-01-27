a, b, c, d = map(int, input().split())

if 1 <= a <= 100 and 1 <= b <= 100 and 1 <= c <= 100 and 1 <= d <= 100:

    if a + b > c and b + c > a and a + c > b:
        print('S')

    elif b + c > d and c + d > b and d + b > c:
        print('S')

    elif a + d > c and a + c > d and c + d > a:
        print('S')

    elif b + a > d and d + a > b and d + b > a:
        print('S')

    else:
        print('N')
