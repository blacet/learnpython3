def my_abs(x):
	if not isinstance(x,(int ,float)):
		raise TypeError("bad operand type")
	if x>= 0:
		return x
	else:
		return -x
import math
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny	

def quadratic(a,b,c):
	if a != 0:
		x1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
		x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
		return x1,x2
		
	
	
print(my_abs(100))
print(my_abs(-200))
#print(my_abs('300'))

x, y = move(100,100,60,math.pi / 6)
print(x,y)

r = move(100,100,60,math.pi / 6)
print(r)

print(quadratic(2,3,1)) # => (-0.5, -1.0)
print(quadratic(1,3,-4)) # => (1.0, -4.0)