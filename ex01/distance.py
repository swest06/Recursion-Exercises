import math

def distance(x1,y1,x2,y2):
        a = (x1 - x2) * (x1 - x2)
        b = (y1 - y2) * (y1 - y2)
        result = math.sqrt(a + b)
	return result
