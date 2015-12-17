import inputs, itertools
from collections import defaultdict
counts = defaultdict(int)
def day17(in_, total_, depth):
	global counts
	test = total_ - in_[0]
	# print('inputs', in_, total_)
	if len(in_)==1:
		# print('one')
		if test==0:
			counts[depth] += 1
		return int(test == 0)
	elif test == 0:
		counts[depth] += 1
		return 1 + day17(in_[1:], total_, depth)
	elif test > 0:
		# print('test>0')
		use = day17(in_[1:], test, depth+1)
		skip = day17(in_[1:], total_, depth)		
		return  use + skip 
	else:
		# print('else')
		skip = day17(in_[1:], total_, depth)
		# print('else done', in_[0], skip)
		return skip

t_ =  [20, 15, 10, 5, 5]

# print(day17(t_, 25))
print(day17(inputs.day17, 150, 0))
m =min(counts.keys())
print('smallest number of jars', m,'in', counts[m], 'different ways')