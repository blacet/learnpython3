list(range(1, 11))
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

[x * x for x in range(1, 11)]
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

[x * x for x in range(1, 11) if x % 2 == 0]
#[4, 16, 36, 64, 100]

[m + n for m in 'ABC' for n in 'XYZ']
#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
	print(k, '=', v)
'''
y = B
x = A
z = C
'''

d = {'x': 'A', 'y': 'B', 'z': 'C' }
[k + '=' + v for k, v in d.items()]
#['y=B', 'x=A', 'z=C']

L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]
#['hello', 'world', 'ibm', 'apple']

#-*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
# 期待输出: ['hello', 'world', 'apple']
L2 = [s.lower() for s in L1 if isinstance(s ,str)]
print(L2)