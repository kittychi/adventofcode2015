constA = 252533
constB = 33554393

row = 2978 
col = 3083

def day25(start, row, col):
	target = sum(range(1, row + col)) - row +1
	code = start
	for i in range(1, target):
		code = (code * constA) % constB
		# print(i, code)
	print(code)

start = 20151125
day25(start, row, col)