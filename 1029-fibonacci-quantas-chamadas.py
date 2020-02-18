call = [0,0,2]
for i in range(3, 40):
    call.append(call[i-1] + call[i-2] + 2)

fibo = [0,1,1]
for i in range(3,40):
    fibo.append(fibo[i-1] + fibo[i-2])

for i in range(int(input())):
    num = int(input())
    print('fib({}) = {} calls = {}'.format(num, call[num], fibo[num]))