import inputs

def getfunction(x):
	return {
	'AND': lambda y, z: y & z , 
	'OR': lambda y, z: y | z, 
	'LSHIFT': lambda y, z: y << z, 
	'RSHIFT': lambda y, z: y >> z, 
	'NOT': lambda z: ~z, 
	'EQ': lambda z: z}.get(x)

def day72(instructions):
	wires = {}
	known = {}
	wireoutputs = {}       
	for instruct in instructions:
		left, out1 = instruct.split(' -> ')
		if 'AND' in left or 'OR' in left or 'LSHIFT' in left or 'RSHIFT' in left:
			in1, fn, in2 = left.split()
			wireoutputs.setdefault(in1, []).append(out1)
			wireoutputs.setdefault(in2, []).append(out1)
			wires[out1] = [fn, [in1, in2]]
		elif 'NOT' in left:
			fn, in1 = left.split()
			wireoutputs.setdefault(in1, []).append(out1)
			wires[out1] = [fn, [in1]]
		else:
			if left.isdigit():
				known[out1] = int(left)
			else:
				wires[out1] = ['EQ', [left]]
				wireoutputs.setdefault(left, []).append(out1)

	while 'a' not in known: 
		outputsofknown = [wireoutputs[a] for a in known]
		tocheck = [a for sublist in outputsofknown for a in sublist if a not in known]
		for w in tocheck: 
			gate, inputs = wires[w]
			in_ = []
			for i in inputs:
				if i.isdigit():
					in_.append(int(i))
				elif i in known:
					in_.append(known[i])
			if (len(in_) == len(inputs)):
				known[w] = getfunction(gate)(*in_)
	print(known['a'])
	
day72(inputs.day7)

day72(inputs.day7b)