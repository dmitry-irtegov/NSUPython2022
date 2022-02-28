def createDictFromFile(filepath):
	"""
	The function takes the path to the English-Latin dictionary file
	and returns a Latin-English dictionary

	:param str filepath: The path to the dictionary file
	"""
	dictionary = {}
	with open(filepath) as dict_file:
		for line in dict_file:
			eng_key, lat_values = line.strip().split(' - ')
			lat_values = lat_values.split(', ')

			for lat_key in lat_values:
				eng_values = dictionary.get(lat_key, [])
				eng_values.append(eng_key)
				dictionary[lat_key] = eng_values

	for lat_key in dictionary:
		dictionary[lat_key].sort()

	return dictionary


if __name__ == '__main__':
	filepath = input()
	dictionary = createDictFromFile(filepath)
	for lat_key in sorted(dictionary.keys()):
		print(f'{lat_key} - {", ".join(dictionary[lat_key])}')
