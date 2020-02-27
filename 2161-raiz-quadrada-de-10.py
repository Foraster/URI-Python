num = int(input())
result = 0
while num != 0:
    result += 6.0
    result = 1.0/result
    num -=1

result += 3.0
print('{:.10f}'.format(result))