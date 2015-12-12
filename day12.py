import re, inputs, json
strings = []
def day12(in_):
	j = json.loads(in_)
	flatten(j)
	numbers = list(map(numberfy, strings))
	
	# p = re.compile(r'-*[0-9]+')
	# numbers = list(p.findall(in_))
	print(numbers)

	print(sum(map(int, numbers)))

def numberfy(x):
	if isinstance(x, int) or x.isdigit():
		return int(x)
	else:
		return 0

def flatten(j):
	isDict = isinstance(j, dict)

	for a in j: 
		val = j[a] if isDict else a
		if isinstance(val, dict):
			if 'red' in list(val.values()):
				continue
			flatten(val)
		elif isinstance(val, list):
			flatten(val)
		elif isinstance(val, int) or isinstance(val, str):
			strings.append(val)
	
day12(inputs.day12)