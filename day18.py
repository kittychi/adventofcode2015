import inputs, ryanInput

lights =[]
inlen = 0

def day18(in_, n, debug=False, b = False):
	global lights, inlen
	lines = in_.split('\n')
	inlen = len(lines)
	lights =  [[[False, False] for a in range(0, inlen+2)] for b in range(0, inlen+2)]
	i = j = 1
	for line in lines:
		for c in line:
			lights[i][j][0] = c == '#'
			j+=1
		j = 1
		i+= 1
	if b:
		lights[1][inlen][0] = lights[1][1][0] = lights[inlen][1][0] = lights[inlen][inlen][0] = True
	iterate(n, debug, b)
	last = [[light for row in lights for light, _ in row], [light for row in lights for _, light in row]]
	print(sum(last[n%2]))


def iterate(numiter, doprint= False, b = False):
	for n in range(0, numiter):
		cur = n % 2
		if doprint:
			printgen(cur)
		for i in range(1, inlen+1):
			for j in range(1, inlen+1):
				calnext(cur, i, j, b)
		last = [[light for row in lights for light, _ in row], [light for row in lights for _, light in row]]
		print('cur=',n, sum(last[cur%2]), 'next=', sum(last[1-cur%2]))	

def calnext(cur, i, j, b = False):
	if  b and ((i == j == 1) or (i == 1 and j == inlen) or (i == inlen and j == 1) or (i == j == inlen)):
		lights[i][j][1-cur] = True
	else:
		coords= [[-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]]
		neighbors = list(map(lambda x, y: lights[(x+i)][(y+j)][cur], coords[0], coords[1]))
		count = sum(neighbors)
		lights[i][j][1-cur] = (lights[i][j][cur] and (count == 2 or count == 3)) or ((not lights[i][j][cur]) and (count == 3))

def printgen(cur):
	for i in range(0, len(lights)):
		s = ''
		for j in range(0, len(lights)):
			if (lights[i][j][cur]):
				s+='#'
			else:
				s+='.'
		print(s)
	print('')

test = '''.#.#.#
...##.
#....#
..#...
#.#..#
####..'''

# day18(test, 10)



# print('')

# for i in range(1, inlen+1):
# 	s = ''
# 	for j in range(1, len(lights)-1):
# 		if (lights[i][j][1]):
# 			s+='#'
# 		else:
# 			s+='.'
# # 	print(s)
day18(inputs.day18,100, b = True)
# day18(ryanInput.i, 100)