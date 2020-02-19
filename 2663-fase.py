n =int(input())
x = int(input())
soma = 0
cont = 0
a = [0 for i in range(n)]
for i in range(n):
    a[i] = int(input())
a.sort(reverse=True)
a.append(-1)
for i in range(n):
    if i<n:
      if a[i]==a[i+1]:
          soma += a.count(a[i])
    if soma>=x:
      break
print(soma)