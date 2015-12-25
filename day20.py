import inputs
from functools import reduce

def day20(in_):
	house = 831600
	factors = getfactors(house)
	print(house, sum(factors), factors)
	while sum(factors) < in_/11:
		print(house, sum(factors), factors)
		house += 1
		factors = getfactors(house)
	print(house, sum(factors), factors)


def getfactors(n): 
	return list(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if (n % i == 0 and (i <= 50 or n//i <= 50)))))

day20(36000000)

