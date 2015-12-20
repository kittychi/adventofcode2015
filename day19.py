import inputs, re
def day19(r_, in_):
	rules = []
	for r in r_.split('\n'):
		find, replace = r.split(' => ')
		rules.append((find.strip(), replace.strip()))

	molecules = set()

	for f, r in rules: 
	# f, r = rules[0]
		starts = [(m.start(), m.end()) for m in re.finditer(f, in_)]
		for s, e in starts: 
			old = in_[:s]
			new = in_[s:]
			replaced = new.replace(f, r, 1)
			molecules.add(old+replaced)
	print(len(molecules))

def day19b(r_, in_):
	rules = []
	for r in r_.split('\n'):
		find, replace = r.split(' => ')
		rules.append((find.strip(), replace.strip()))

	dfs(rules, in_, 0)

found = False

def dfs(rules, molecules, depth):
	global found
	found = molecules == 'e'
	if found:
		print(depth)
		return
	for f, r in rules: 
		if r in molecules: 
			# print('replacing', r, 'with', f)
			reduced = molecules.replace(r, f, 1)
			print(depth, 'replacing', r, 'with', f)
			print(reduced)
			dfs(rules, reduced, depth+1)
			if found:
				return
		# else:
			# print(r)



# day19(inputs.d19rules, inputs.d19in)

rules = '''e => H
e => O
H => HO
H => OH
O => HH'''
from ryanInput import d19r, d19i
# day19b(rules, 'HOHOHO')
# day19b(inputs.d19rules, inputs.d19in)
day19b(d19r, d19i)