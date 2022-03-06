def get_pythagorean_triples(limit):
	"""
	Return Pythagorean triples where all numbers are at most limit

	:param limit: maximum value of triplet element
	:return: list of triplets
	"""
	return [
		(m*m - n*n, 2 * m * n, m*m + n*n) 
		for m in range(2, limit)
		for n in range(1, m) 
		if m*m + n*n <= limit
	]

if __name__ == '__main__':
	number = int(input())
	print(get_pythagorean_triples(number))
