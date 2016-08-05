#map/reduce
#但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：

from functools import reduce
def fn(x, y):
	return x * 10 + y

reduce(fn, [1, 3, 5, 7, 9])
#13579
#这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：

from functools import reduce
def fn(x, y):
	return x * 10 + y

def char2num(s):
	#前面{‘key’：value}是一个dict，value = dict[key]就是根据key取value
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

reduce(fn, map(char2num, '13579'))
#13579

#整理成一个str2int的函数就是：
from functools import reduce
def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn, map(char2num, s))

str2int('13579')
#13579







