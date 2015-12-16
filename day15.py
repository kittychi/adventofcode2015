import inputs, itertools, re, functools
def day15(in_):
	ingredients = {}
	portions = []
	p = re.compile(r'([A-Za-z]+): capacity (-*[0-9]+), durability (-*[0-9]+), flavor (-*[0-9]+), texture (-*[0-9]+), calories (-*[0-9]+)')
	i = 0
	for name, cap, dur, flav, text, cal in p.findall(in_):
		ingredients[name] = (i, [int(cap), int(dur), int(flav), int(text), int(cal)])
		portions.append(0)
		i += 1
	print(ingredients)

	combinations = list(itertools.combinations_with_replacement(range(0, 101), len(ingredients.keys())))
	print('len', len(combinations))
	# combinations = [(1, 1, 1, 97)]
	maxscore = 0
	maxportions = []
	combo = [0] *len(ingredients)
	while increment(combo, len(ingredients)-1):
		if sum(combo) != 100:
			continue
		portionstats = {} 
		print(combo)
		# print(ingredients.values())
		for i, stats in ingredients.values(): 
			# print(i, stats)
			portionstats[i] = list(map(lambda x: combo[i] * x, stats))
		# print('pstats',portionstats)
		category_ = list(zip(*portionstats.values()))
		# print('cat', category_)
		summed = list(map(lambda x: sum(x), category_))
		if len(list(filter(lambda x: x < 0, summed[:-1]))) > 0 or summed[-1] != 500:
			continue
		# print('cat', category_)
		total = functools.reduce(lambda x, y: x*y, summed[:-1], 1)
		# print(summed)
		# print(total)
		if total > maxscore:
			maxscore = total
			maxportions = [a for a in combo]
		
	print(maxscore)
	print(maxportions)

def increment(chars, index):
	if index < 0:
		return False
	chars[index]+=1
	if chars[index]>100:
		chars[index] = 0
		return increment(chars, index-1)
	return True
day15(inputs.day15)