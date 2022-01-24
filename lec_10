data_set=[(0,1),(1,2),(2,4)]
n=len(data_set)
def L0(x):
	val=1
	val=(x-data_set[1][0])/(data_set[0][0]-data_set[1][0])*(x-data_set[2][0])/(data_set[0][0]-data_set[2][0])
	return val

def L1(x):
	val=1
	val=(x-data_set[2][0])/(data_set[1][0]-data_set[2][0])*(x-data_set[0][0])/(data_set[1][0]-data_set[0][0])
	return val

def L2(x):
	val=1
	val=(x-data_set[0][0])/(data_set[2][0]-data_set[0][0])*(x-data_set[1][0])/(data_set[2][0]-data_set[1][0])
	return val	

def P(x):
	res=data_set[0][1]*(x-data_set[1][0])/(data_set[0][0]-data_set[1][0])*(x-data_set[2][0])/(data_set[0][0]-data_set[2][0])
	res+=data_set[1][1]*(x-data_set[2][0])/(data_set[1][0]-data_set[2][0])*(x-data_set[0][0])/(data_set[1][0]-data_set[0][0])
	res+=data_set[2][1]*(x-data_set[0][0])/(data_set[2][0]-data_set[0][0])*(x-data_set[1][0])/(data_set[2][0]-data_set[1][0])
	return res
print("Enter the value where you want to find the value of interpolation")
inp=float(input())
ans=P(inp)
print("The interpolated value at x=1.5 is ",ans)
print("Percentage error in interpolation is",100*(2**inp-ans)/2**inp)
