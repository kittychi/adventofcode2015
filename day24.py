import inputs, itertools
from collections import defaultdict
from functools import reduce
def day24(in_, numgroups):
	target = sum(in_) // numgroups
	subsets = []
	reverselist = list(reversed(in_))
	
	subsets = findtarget(reverselist, target)
	print(subsets)
	groupsize = {}
	if numgroups == 3:
		groupsize = partone(subsets, reverselist, target)
	elif numgroups == 4:
		groupsize = parttwo(subsets, reverselist, target)
	
	minlength = min(groupsize.keys())

	print(groupsize[minlength])
	qe = []
	for group in groupsize[minlength]:
		qe.append(reduce(lambda x, y: x * y, group))
	
	print(min(qe), qe)

def day24a(in_, numgroups):
	target = sum(in_) // numgroups
	p1 = []
	for i in range(0, len(in_)):
		print(i)
		subset = list(itertools.combinations(in_, i))
		p1 = [a for a in subset if sum(list(a)) == target]
		if p1 != []:
			break
	qe = []
	for p in p1: 
		qe.append(reduce(lambda x, y: x*y, p))
	print(min(qe), qe)


def partone(subsets, in_, target):
	groupsize = defaultdict(set)
	for group in subsets: 
		remaining = [a for a in in_ if a not in group]
		if sum(remaining) // 2 == target:
			package2 = findtarget(remaining, target)
			for p2 in package2: 
				p3 = [a for a in remaining if a not in p2]
				groupsize[len(group)].add(tuple(group))
				groupsize[len(p2)].add(tuple(p2))
				groupsize[len(p3)].add(tuple(p3))
				print(group, p2, p3)

	return groupsize

def parttwo(subsets, in_, target):
	groupsize = defaultdict(set)
	for p1 in subsets: 
		remaining = [a for a in in_ if a not in p1]
		package2 = findtarget(remaining, target)
		for p2 in package2: 
			remaining2 = [a for a in remaining if a not in p2]
			package3 = findtarget(remaining2, target)
			for p3 in package3:
				p4 = [a for a in remaining2 if a not in p3]
				groupsize[len(p1)].add(tuple(p1))
				groupsize[len(p2)].add(tuple(p2))
				groupsize[len(p3)].add(tuple(p3))
				groupsize[len(p4)].add(tuple(p4))
				print(p1, p2, p3, p4)
	return groupsize

def findtarget(l_, num):
	subsets = []
	for j in range(0, len(l_)):
		test = l_[j:]
		numbers = []
		cursum = 0
		for i in range(0, len(test)):
			if cursum + test[i] <= num:
				cursum += test[i]
				numbers.append(test[i])
			if cursum == num:
				subsets.append(numbers) 
				break
	return subsets
# day24(inputs.d24, 3)

day24a(inputs.d24, 4)