import inputs, itertools, math
def day21(boss, hp):
	w_ = [tuple(map(int,(weapon.split()[1:]))) for weapon in inputs.weapons.split('\n')]
	a_ = [tuple(map(int,(armor.split()[1:]))) for armor in inputs.armor.split('\n')]
	r = [tuple(map(int,ring.split()[2:])) for ring in inputs.rings.split('\n')]
	print(w_)
	print(a_)
	r.append((0,0,0))	
	mincost = math.inf
	maxcost = -math.inf
	for w in w_: 
		for r1 in r:
			otherrings = r[:]
			otherrings.remove(r1)
			for r2 in otherrings: 
				cost, atk, defs = tuple(map(sum,zip(r1, w, r1, r2)))
				if (boss[1]-defs) - (atk -boss[2]) > 0 and cost > maxcost:
					maxcost = cost
					print('max', cost, w, r1, r2)
				elif (boss[1]-defs) - (atk -boss[2]) <= 0 and cost < mincost:
					mincost = cost
					print('min', cost, w, r1, r2)
				# print('n', cost, atk, defs)
				for a in a_: 
					costa, atka, defsa = tuple(map(sum, zip(a, (cost, atk, defs))))
					# print(' ', armor)
					if (boss[1]-defsa) - (atka -boss[2]) > 0 and costa > maxcost:
						maxcost = costa
						print('max',costa, w, r1, r2,a)
					elif (boss[1]-defsa) - (atka -boss[2]) <= 0 and costa < mincost:
						mincost = costa
						print('min',costa, w, r1, r2, a)
	print(maxcost, mincost)




day21(inputs.d21boss, 100)