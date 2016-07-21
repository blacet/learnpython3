d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
d['Adam'] = 67
print(d['Adam'])
print(d)

d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])
b = 'Thomas' in d
print('Key \'Thomas\' in dict d？:%s' % ('Thomas' in d) )