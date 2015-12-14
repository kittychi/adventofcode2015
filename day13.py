import inputs, itertools
from collections import defaultdict
def day13(in_, b = False):
	nodes = set()
	relation = defaultdict(dict)
	for line in in_:
		p1, _, d, val, _, _, _, _,_,_,p2 = line.split()
		p2 = p2[:-1]
		nodes.add(p1)
		nodes.add(p2)
		relation[p1].setdefault(p2, 0) 
		relation[p1][p2] += int(val) if d == 'gain' else -int(val)
		relation[p2][p1] = relation[p1][p2]

	#part b
	if b:
		relation['me'] = {}
		for p in nodes:
			relation[p]['me']=0
			relation['me'][p] = 0
		nodes.add('me')

	allcombos = list(itertools.permutations(list(nodes)[:-1]))
	removed = list(nodes)[-1]
	allhapdelta = {}
	for combo in allcombos:
		first = list(combo)
		first.append(removed)
		next = [first[i%len(first)] for i in range(1, len(first)+1)]
		pairs = list(zip(first, next))
		hap_ = [relation[x][y] for x, y in pairs]
		allhapdelta.setdefault(sum(hap_), []).append(first)

	sort = sorted(allhapdelta.items(), reverse=True)
	for h, li_ in sort[0:3]:
		print(h)
		for l in li_:
			first = list(l)
			neighbour = [first[i%len(first)] for i in range(1, len(first)+1)]
			pairs = list(zip(first, neighbour))
			hap_ = [relation[x][y] for x, y in pairs]
			print( list(zip(first, hap_)))

day13(inputs.day13)
print('b')
day13(inputs.day13, True)
