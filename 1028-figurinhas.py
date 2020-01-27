def mdc(f1,f2):
    if f2 == 0:
        return f1
    else:
        return mdc(f2, f1 % f2)

qnt = int(input())

for i in range(qnt):
    f1, f2 = map(int, input().split())
    print(mdc(f1,f2))
