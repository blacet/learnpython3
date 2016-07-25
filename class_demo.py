#class demo

class Student(object):#bojcet是父类
	def __init__(self,name,score):#self是显示传入的当前实例对象，类似this
		self.name = name
		self.score = score
	
	def print_score(self):
		print('%s :%s '%(self.name, self.score))

bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()