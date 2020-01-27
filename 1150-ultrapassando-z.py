j = 1
x = int(input())
z = int(input())
while z <= x:
    z = int(input())

for i in range(x, z+1):
    x += i
    j += 1
    if x > z:
        break

print(j)