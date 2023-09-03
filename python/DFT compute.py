import math
def compute(inreal, inimag):
	assert len(inreal) == len(inimag)
	n = len(inreal)
	outreal = []
	outimag = []
	for k in range(n):
		sumreal = 0.0
		sumimag = 0.0
		for t in range(n):  
			angle = 2 * math.pi * t * k / n
			sumreal +=  inreal[t] * math.cos(angle) + inimag[t] * math.sin(angle)
			sumimag += -inreal[t] * math.sin(angle) + inimag[t] * math.cos(angle)
		outreal.append(sumreal)
		outimag.append(sumimag)
	return (outreal,outimag)
print("real number:       image number:")
print(compute([1,2,3,4],[1,2,3,4]))