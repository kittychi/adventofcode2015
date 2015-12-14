import inputs, re, itertools
from collections import namedtuple
def day14(in_, t_):
	Reindeer = namedtuple('Reindeer', ['name', 'speed', 'endurance', 'rest'])
	R = []
	r = re.compile(r'(\w*) can fly (\d*) km/s for (\d*) seconds, but then must rest for (\d*) seconds.')
	for name, speed, time, rest in r.findall(in_):
		R.append(Reindeer(name, int(speed), int(time), int(rest)))
		
	result = {}
	for i in range(1, t_+1):
		# print(i)
		dist = {}
		for r in R:
			seconds = r.endurance * (i // (r.endurance + r.rest))
			lastLeg = i % (r.endurance + r.rest)
			seconds += lastLeg if lastLeg <= r.endurance else r.endurance
			dist.setdefault(seconds * r.speed, []).append(r.name)
		# print( sorted(dist.items(), reverse = True))
		maxdist = max(dist.keys())
		for j in dist[maxdist]:
			result.setdefault(j, 0)
			result[j] += 1
		# print(result)
	
	print(result.items())
	print(dist.items())
	print(max(result.values()))

day14(inputs.day14, inputs.day14time)