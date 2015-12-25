import inputs

def day1(strInput):
	up = 0
	down = 0
	for i in range(0, len(strInput)):
		if strInput[i] == '(':
			up = up + 1
		elif strInput[i] == ')':
			down = down+1
		else:
			continue
		if down > up:
			print (i + 1)
			break

# day1(inputs.day1)

def day2(dimensionlist):
	totalsqft = 0
	totalribbon = 0
	for box in dimensionlist:
		dimensions = box.split('x')
		dimensions = [int(i) for i in dimensions]
		totalsqft += boxArea(dimensions)
		totalribbon += ribbonlength(dimensions)
	print ('wrapping paper: ',totalsqft)
	print ('ribbon:', totalribbon)

def boxArea(dimList):
	l, w, h = dimList
	lw = l*w
	wh = w*h
	hl = h*l
	return 2*(lw+wh+hl) + min(lw, wh, hl)

def ribbonlength(dimList):
	l,w,h = dimList
	perimeter = (sum(dimList) - max(dimList))*2
	return l*w*h + perimeter
	
# day2(inputs.day2)

def day3a(strInput):
	totalHouses = len(strInput) + 1
	houses = {(0, 0):1}
	cur = (0, 0)
	for i in range(0, len(strInput)):
		direction = dir(strInput[i])
		newpos = tuple(map(lambda x, y: x+y, cur, direction))
		if newpos in houses:
			houses[newpos] += 1
		else:
			houses[newpos] = 1
		cur = newpos
	multipleVisits = [house for house in houses if houses[house] > 1]
	totalHouseVisited = len(houses)
	print ('total houses',totalHouses, 'visited', totalHouseVisited)

def day3b(strInput):
	houses = {(0, 0):2}
	curlist = [('santa',(0,0)), ('robo',(0,0))]
	for i in range(0, len(strInput)):
		name, cur = curlist[i%2]
		direction = dir(strInput[i])
		newpos = tuple(map(lambda x, y: x+y, cur, direction))
		if newpos in houses:
			houses[newpos] += 1
		else:
			houses[newpos] = 1
		curlist[i%2] = (name, newpos)
	totalHouseVisited = len(houses)
	print ('visited', totalHouseVisited)


def dir(x):
	return {
	'^':(0, 1),
	'v':(0, -1),
	'<':(-1, 0),
	'>':(1, 0)
	}.get(x, (0, 0))

input3test1 = '^v'
input3test2 = '^>v<'
input3test3 = '^v^v^v^v^v'

# day3a(inputs.day3)

# day3b(inputs.day3)

import hashlib

def day4(secret):
	i = 0
	while True: 
		key = secret+str(i)
		hashed = hashlib.md5(str.encode(key)).hexdigest()
		if hashed.startswith('000000'):
			print(i)
			break
		else: 
			i += 1

#day4(input.day4)

import re

def day5(strings):
	nice = []
	naughty = []
	for s in strings: 
		vowels = re.findall('[aeiou]', s)
		repeated = [m for m in re.finditer(r'((\w)\2)+', s)]
		invalid = re.findall('(ab)|(cd)|(pq)|(xy)',s)

		if len(vowels) < 3 or len(repeated) == 0 or len(invalid) > 0:
			naughty.append(s)
		else:
			nice.append(s)
	print('nice', len(nice), 'naughty', len(naughty))
	print(nice, naughty)

test = ['jchzalrnumimnmhp','ugknbfddgicrmopn', 'aaa', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']

#day5(input.day5)

def day5b(strings):
	nice=[]
	naughty = []
	for s in strings:
		repeatgroup = [m for m in re.finditer(r'([a-z]{2})[a-z]*\1', s)]
		repeatletter = [m for m in re.finditer(r'(\w)[a-z]\1', s)]
		
		if len(repeatgroup) > 0 and len(repeatletter) >0:
			nice.append(s)
		else:
			naughty.append(s)		
	print(len(nice))
	print(nice, naughty)

# day5b(inputs.day5)

def day6(instructions):
	on = set()
	brightness = {}
	for instruction in instructions:
		command, start, through, end = instruction.split(' ')
		startx, starty = start.split(',')
		endx, endy = end.split(',')
		if command == 'on':
			for x in range(int(startx), int(endx)+1):
				for y in range(int(starty), int(endy)+1):
					coord = str(x)+','+str(y)
					brightness[coord] = 1 if coord not in list(brightness.keys()) else brightness[coord]+1
					on.add(coord)
		elif command =='off':
			for x in range(int(startx), int(endx)+1):
				for y in range(int(starty), int(endy)+1):
					coord = str(x)+','+str(y)
					if coord in on: on.remove(coord)
					if coord in list(brightness.keys()):
						brightness[coord] -= 1
						if brightness[coord] == 0:
							brightness.pop(coord)
		elif command == 'toggle':
			for x in range(int(startx), int(endx)+1):
				for y in range(int(starty), int(endy)+1):
					coord = str(x)+','+str(y)
					brightness[coord] = 2 if coord not in list(brightness.keys()) else brightness[coord]+1
					if coord in on:
						on.remove(coord)
					else:
						on.add(coord)
	print (len(on))
	print (sum(brightness.values()))

# # test = ['on 0,0 through 1,1', 'toggle 1,1 through 1,3']
# day6(test)
day6(inputs.day6)