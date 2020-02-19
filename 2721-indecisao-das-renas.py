renas = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']
print(renas[(sum(list(map(int, input().split()))) % 9)-1])


