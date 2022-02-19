def get_pythagorean_triples(n):
	"""
	Return all Pythagorean triples where all numbers are at most n
	"""
	return [
		(a, b, c) 
		for a in range(1, n + 1)
		for b in range(1, n + 1) 
		for c in range(1, n + 1)
		if a <= b and a ** 2 + b ** 2 == c ** 2
	]

if __name__ == '__main__':
	number = int(input())
	print(get_pythagorean_triples(number))
