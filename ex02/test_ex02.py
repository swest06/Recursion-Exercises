from power import power

def test_one():
	assert power(2,-3) == 0.125

def test_two():
	assert power(2,1) == 2 

def test_three():
	assert power(2,2) == 4

def test_four():
	assert power(2,3) == 8

def test_five():
	assert power(2,4) == 16

def test_six():
	assert power(2,9) == 512

def test_seven():
	assert power(2,10) == 1024

def test_eight():
	assert power(2,15) == 32768

def test_nine():
	assert power(2,0) == 1

def test_ten():
	assert power(3,1) == 3

def test_eleven():
	assert power(3,2) == 9

def test_twelve():
	assert power(3,3) == 27

def test_thirteen():
	assert power(3,10) == 59049

def test_fourteen():
	assert power(3,0) == 1

def test_fifteen():
	assert power(1.1414,2) == 1.30279

def test_sixteen():
	assert power(1.5,10) == 57.665

def test_seventeen():
	assert power(1,-1) == 1

def test_eighteen():
	assert power(2,-1) == 0.5

def test_nineteen():
	assert power(2,-2) == 0.25

def test_twenty():
	assert power(2,-3) == 0.125

def test_twentyone():
	assert power(2,-4) == 0.0625

def test_twentytwo():
	assert power(2,-8) == 0.00390625

def test_twentythree():
	assert power(2,-9) == 0.00195312

def test_twentyfour():
	assert power(2,-10) == 0.000976562

def test_twentyfive():
	assert power(2,-15) == 3.05176e-05

def test_twentysix():
	assert power(3,-1) == 0.333333

def test_twentyseven():
	assert power(3,-2) == 0.111111

def test_twentyeight():
	assert power(3,-3) == 0.037037

def test_twentynine():
	assert power(3,-4) == 0.0123457

def test_thirty():
	assert power(3,-5) == 0.00411523

def test_thirtyone():
	assert power(3,-10) == 1.69351e-05

def test_thirtytwo():
	assert power(3,-6) == 0.00137174

def test_thirtythree():
	assert power(1.1414,-2) == 0.767581

def test_thirtyfour():
	assert power(1.5,-10) == 0.0173415
