a = 15
b = a/2
c = 15.456
d = c/7

print('Valores de b:')
print('-------------')
print('1) b =', int(b))
print('2) b =                   ', int(b))
print('3) b = 0000000000000000000{}'.format(int(b)))
print('4) b = {}                   '.format(int(b)))
print('5) b = {}%'.format(int(b)))
print()
print('Valores de d:')
print('-------------')
print('1) d = %.6f' %d)
print('2) d =', int(d))
print('3) d = %.1f' %d)
print('4) d = %.2f' %d)
print('5) d = %.3f' %d)
print('6) d =                {:.4}'.format(d))
print('7) d = 000000000000000{:.4}'.format(d))
print('8) d = {:.4}               '.format(d))
print('9) d = {:.3}%'.format(d))