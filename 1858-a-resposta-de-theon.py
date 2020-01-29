n = int(input())
num = list(map(int, input().split()))
menor = min(num)
print(num.index(menor)+1)