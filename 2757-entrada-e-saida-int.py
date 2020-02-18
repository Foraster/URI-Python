A = int(input())
B = int(input())
C = int(input())

print('A = {}, B = {}, C = {}'.format(A,B,C))
print('A = {:10}, B = {:10}, C = {:10}'.format(A,B,C))
print('A = %s, B = %s, C = %s' % (str(A).zfill(10), str(B).zfill(10), str(C).zfill(10)))
print('A = {:<10}, B = {:<10}, C = {:<10}'.format(A,B,C))
