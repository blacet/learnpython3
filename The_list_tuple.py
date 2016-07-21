#list是一个可变的有序表 list是用[]括起来的
classmates = ['Michael','Bob','Tracy']
print('classmates初始化后：',classmates)
#计算list长度
print('classmates的长度: %d = len(classmates)' % len(classmates))
#取第一个元素
print('取第一个元素classmates[0]:',classmates[0])
#取倒数第一个元素
print('取倒数第一个元素classmates[-1]:',classmates[-1])
#往list中追加元素到末尾
print('往list中追加元素到末尾classmates.append(\'Adam\')')
classmates.append('Adam')
print(classmates)
#也可以把元素插入到指定的位置，比如索引号为1的位置：
print('也可以把元素插入到指定的位置，比如索引号为1的位置classmates.insert(1,\'Jack\')')
classmates.insert(1,'Jack')
print(classmates)
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
print('要删除指定位置的元素，用pop(i)方法，其中i是索引位置classmates.pop(1)')
classmates.pop(1)
print(classmates)
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
print('要把某个元素替换成别的元素，可以直接赋值给对应的索引位置classmates[1]= \'Sarah\'')
classmates[1] = 'Sarah'
print(classmates)
#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
#tuple 是用()括起来的
print('另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改')
classmates=('Michael', 'Bob', 'Tracy')
print(classmates)
#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t =(1,)