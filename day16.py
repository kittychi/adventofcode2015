import inputs, re
def day16(tape_, sue_, lt_ = '', gt_ = ''):
	s_ = re.compile(r'Sue ([0-9]+): ([a-z :,0-9]+)')
	t_ = re.compile(r'([a-z]+): ([0-9]+)')
	sues = s_.findall(sue_)
	targets = t_.findall(tape_)
	lt = lt_.split()
	gt = gt_.split()
	print(lt, gt)
	qualified = {}
	match = {}
	for category, count in targets:
		match[category.strip()] = int(count)

	candidate = set([a for a in range(1, 501)])
	print(candidate)
	for sue, items in sues: 
		itemlist = items.split(',')
		for i in itemlist:
			item, count = i.split(':')
			if (item.strip() in lt and int(count) < match[item.strip()]) or (item.strip() in gt and int(count) > match[item.strip()]) or int(count) == match[item.strip()]:
				continue
			candidate.discard(int(sue))
	print(candidate)
day16(inputs.day16tape, inputs.day16sue)
day16(inputs.day16tape, inputs.day16sue, inputs.day16lt, inputs.day16gt)