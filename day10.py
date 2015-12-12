import inputs
def day10(start):
	print (start)
	iteration = start
	for i in range(0, 50):
		index = 0
		next = ''
		curdig = iteration[0]
		count = 1
		index  += 1
		while index < len(iteration):
			if curdig == iteration[index]:
				count+=1
			else:
				next += str(count)+str(curdig)
				curdig = iteration[index]
				count = 1
			index+=1
		next += str(count)+str(curdig)
		# print(i, next)
		iteration = next

	print(len(next))
day10(inputs.day10)
