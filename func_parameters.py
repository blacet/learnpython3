#函数参数
#1、位置参数
'''
def power(x):
	return x*x
print(power(5))
'''
"""
#2、
"""
a = '''bbc'''
print(a)

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5,3))


#2、默认参数

def power(x, n = 2):
	s = 1
	while n >0:
		n = n - 1
		s = s*x

print(power(5,3))
#3、


#4、

#5、

