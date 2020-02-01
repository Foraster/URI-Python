F, B, M = map(int, input().split())
Fs, Bs, Ms = map(int, input().split())
total = 0

calc = F - Fs
if calc < 0:
    total += abs(calc)

calc = B - Bs
if calc < 0:
    total += abs(calc)

calc = M - Ms
if calc < 0:
    total += abs(calc)

print(total)