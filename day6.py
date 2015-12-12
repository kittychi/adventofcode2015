import re, itertools, inputs
def onf(c):
	a, b = on[c[0]][c[1]] 
	on[c[0]][c[1]] = (True, b+ 1)
def off(c):
	a, b = on[c[0]][c[1]]
	on[c[0]][c[1]] = (False, max(0, b-1))
def toggle(c):
	a, b = on[c[0]][c[1]]
	on[c[0]][c[1]]= (not a, b+2)

def afunction(command):
	if command == 'on':
		return onf
	elif command == 'off':
		return off
	elif command == 'toggle':
		return toggle

on = [[(False, 0) for i in range(0, 1000)] for j in range(0, 1000)]

def day6(instructions):
	
	allcommands = list(map(lambda x: x.split()[0], instructions))
	getallstartends = lambda y: list(map(lambda x: tuple(map(int, x.split(','))), re.findall(r'[0-9]+,[0-9]+', y)))

	# [[(startx, starty), (endx, endy)], [(sx,sy),(ex,ey),...]]
	allstartends = list(map(getallstartends, instructions))

	for i in range(0, len(instructions)):
		s, e = allstartends[i]
		a = allcommands[i]
		allcoords = list(itertools.product([i for i in range(s[0], e[0]+1)], [j for j in range(s[1], e[1]+1)]))	
		for c in allcoords:
			if a == 'on':
				onf(c)
			elif a == 'off':
				off(c)
			elif a == 'toggle':
				toggle(c)
		
	a = [col[0] for row in on for col in row]
	b = [col[1] for row in on for col in row]
	print(sum(a))
	print(sum(b))
	

t = ['toggle 0,0 through 5,0', 'off 2,0 through 3,1', 'off 1,2 through 4,3']

day6(inputs.day6)

543903
14687245
[Finished in 31.4s]