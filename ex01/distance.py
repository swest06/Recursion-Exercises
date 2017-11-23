import math

def distance(x1,y1,x2,y2):
        a = (x1 - x2)**2
        b = (y1 - y2)**2
        result = round(math.sqrt(a + b), 6)
        return result



