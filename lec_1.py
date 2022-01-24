
def y(x):
	return x**2-10
def y_der(x):
	return 2*x

def root_find(x0):
	x=x0
	for i in range (0,100):
		x=x0-y(x0)/y_der(x0)
		x0=x
	return x

print(root_find(-0.00000001))

