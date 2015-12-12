import math, inputs

def parseInput(input):
	vertex = set()
	edges = {}
	for line in input:
		start, _, end, _, weight = line.split()
		vertex.add(start)
		vertex.add(end)
		if start not in edges:
			edges[start] = {end: int(weight)}  
		else:
			edges[start][end] = int(weight)
		if end not in edges:
			edges[end] = {start: int(weight)}
		else:
			edges[end][start] = int(weight)
	return list(vertex), edges

def day9(input):
	
	vertices, edges  = parseInput(input)

	for i in range(0, len(vertices)):
		visited = []
		info = {city: (math.inf, None) for city in vertices}
		startcity = list(info.keys())[i]
		info[startcity] = (0, None)
		u = None

		while len(visited) != len(vertices):
			unvisited = [city for city in list(info.keys()) if city not in visited]
			mindist = math.inf
			
			for city in unvisited:
				dist, _ = info[city]
				if dist < mindist:
					u = city
					mindist = dist
			visited.append(u)
			neigh = edges[u]
			curmin = math.inf
			v = None
			for n in neigh:
				if n in visited:
					continue
				alt = mindist + neigh[n]
				dist_v, prev_v = info[n]
				if alt < dist_v and alt < curmin:
					curmin = alt
					v = n
			info[v] = (curmin, u)

		dist = [info[c][0] for c in visited] 
		print(visited, dist)
		print ('start at', startcity, max(dist))


def day9b(input):
	
	vertices, edges  = parseInput(input)

	for i in range(0, len(vertices)):
		visited = []
		info = {city: (-1, None) for city in vertices}
		startcity = list(info.keys())[i]
		info[startcity] = (0, None)
		u = None

		while len(visited) != len(vertices):
			unvisited = [city for city in list(info.keys()) if city not in visited]
			maxdist = -1
			
			for city in unvisited:
				dist, _ = info[city]
				if dist > maxdist:
					u = city
					maxdist = dist
			visited.append(u)
			neigh = edges[u]
			curmax = -1
			v = None
			for n in neigh:
				if n in visited:
					continue
				alt = maxdist + neigh[n]
				dist_v, prev_v = info[n]
				if alt > dist_v and alt > curmax:
					curmax = alt
					v = n
			info[v] = (curmax, u)

		dist = [info[c][0] for c in visited] 
		print(visited, dist)
		print ('start at', startcity, max(dist))


day9(inputs.day9)


