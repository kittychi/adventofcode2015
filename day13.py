import inputs, itertools
def day13(in_):
	nodes = set()
	edges = {}
	for line in in_:
		p1, _, d, val, _, _, _, _,_,_,p2 = line.split()
		p2 = p2[:-1]
		nodes.add(p1)
		nodes.add(p2)
		curval = edges.setdefault(p1, {}).setdefault(p2, 0)
		edges[p1][p2] += int(val) if d == 'gain' else -int(val)
		edges.setdefault(p2, {}).setdefault(p1, 0)
		edges[p2][p1] = edges[p1][p2]

	#part b
	edges['me'] = {}
	for p in nodes:
		edges[p]['me']=0
		edges['me'][p] = 0
	nodes.add('me')

	allcombos = list(itertools.permutations(nodes))
	allhapdelta = []
	for combo in allcombos:
		first = list(combo)
		next = [first[i%len(first)] for i in range(1, len(first)+1)]
		pairs = list(zip(first, next))
		hap_ = [edges[x][y] for x, y in pairs]
		allhapdelta.append(sum(hap_))
	print(max(allhapdelta))
day13(inputs.day13)
