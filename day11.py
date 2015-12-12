import inputs, re
def day11(in_):
	#a
	chars = list(map(ord, in_))
	pairs = re.compile(r'.*([a-z])\1.*([a-z])\2')
	while True:

		hasconsec = False
		increment(chars, len(chars)-1)
		password = ''.join(chr(i) for i in chars)
		haspair = pairs.match(password) != None
		for i in range(0,len(chars)-2):
			if i < len(chars)-2 and not hasconsec:
				hasconsec = chars[i+1] == chars[i] + 1 and chars[i+2] == chars[i] +2
			if hasconsec:
				break
		if haspair and hasconsec:
			print(password)
			break

def increment(chars, index):
	if index < 0:
		return
	chars[index]+=1
	if chars[index]>122:
		chars[index] = 97
		increment(chars, index-1)
	if chars[index] in [105, 108, 111]:
		chars[index] += 1


day11('hepxxyzz')