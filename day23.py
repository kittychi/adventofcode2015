import inputs
from collections import defaultdict
def day23(in_):
	registers = defaultdict(int)
	lines = in_.split('\n')
	i = 0
	while i < len(lines):
		print(lines[i], registers)
		line = lines[i].split()
		if 'hlf' in line:
			var = line[1].strip()
			registers[var] //= 2
			i+=1
		elif 'tpl' in line: 
			var = line[1].strip()
			registers[var] *= 3
			i+=1
		elif 'inc' in line:
			var = line[1].strip()
			registers[var] += 1
			i+=1
		elif 'jmp' in line: 
			offset = int(line[1])
			i += offset
		elif 'jie' in line: 
			var = line[1].split(',')[0]
			offset = line[2]
			if registers[var] % 2 == 0:
				i += int(offset)
			else: 
				i+=1
		elif 'jio' in line: 
			var = line[1].split(',')[0]
			offset = line[2]
			if registers[var] == 1: 
				i += int(offset)
			else: 
				i+=1 
		print(registers)

	print(registers)

day23(inputs.d23r)
