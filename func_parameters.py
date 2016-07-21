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
#定义默认参数要牢记一点：默认参数必须指向不变对象！
def power(x, n = 2):
	s = 1
	while n >0:
		n = n - 1
		s = s*x

print(power(5,3))
#3、可变参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
		print(sum)
    return sum

#4、关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30) # name: Michael age: 30 other: {}
person('Adam', 45, gender='M', job='Engineer')#name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

#5、命名关键字参数
#对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
def person(name,age,**kw):
	if 'city' in kw:
		#有city参数
		pass
	if 'job' in kw:
		#有job参数
		pass
	print('name:',name,'age:',age,'other:',kw)

'''
如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)
和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：

'''
#6、参数组合
#这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。




