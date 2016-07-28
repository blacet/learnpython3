>>> type(123)
<class 'int'>
>>> type(str)
<class 'type'>
>>> type('str')
<class 'str'>
>>> type(None)
<class 'NoneType'>
>>> type(abs)
<class 'builtin_function_or_method'>
>>> type(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> type(123)==int
True
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__ha
sh__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setat
tr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isaln
um', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'pa
rtition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

>>>
>>> dir --help
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bad operand type for unary -: '_Helper'
>>> type('abc') == type('123')
True
>>> class Student(object):
...     def __init__(self,name):
...             self.name = name
...
>>> s = Student('Bob')
>>> s.score =90
>>>
>>> s
<__main__.Student object at 0x0053DE70>
>>> s.name
'Bob'
>>> s.score
90
>>> class Student(object):
...     name = 'Student'
...
>>> Student.name
'Student'

>>> s = Studemt()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Studemt' is not defined
>>> s = Student()
>>> s.name
'Student'
>>> Student.name
'Student'
>>> s.name = 'Michael'
>>> s.name
'Michael'
>>> Student.name
'Student'
>>> del s.name
>>> s.name
'Student'
>>> Student.name
'Student'
>>> class Student(object):
...     pass
...
>>> s = Student()
>>> s.name = 'Michael'
>>> s.name
'Michael'
>>> print(s.name)
Michael
>>> def set_age(self,age):
...     self.age = age
...
>>> from types import MethodType
>>> s.set_age = MethodType(set_agems)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'set_agems' is not defined
>>> s.set_age = MethodType(set_age,s)
>>> s.set_age(25)
>>> s.age
25
>>> s2 = Student()
>>> s2.set_age(26)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'set_age'
>>> def set_score(self,score):
...     self.score = score
...
>>> Student.set_score = set_score
>>> s.set_score(100)
>>> s.score
100
>>> s2.set_score(99)
>>> s2.score
99
>>>
