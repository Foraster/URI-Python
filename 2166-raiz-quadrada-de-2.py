def raiz(num):
    if num == 0:
        return 2
    x = 2 + 1 / raiz(num-1)
    return x

result = raiz(int(input()))-1
print('{:.10f}'.format(result))