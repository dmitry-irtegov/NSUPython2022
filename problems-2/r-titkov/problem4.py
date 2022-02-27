import sys

"""
This module takes a sequence of digits and outputs
the number of occurrences of this sequence in the pi.txt file
"""

if __name__ == '__main__':
	try:
		with open("pi.txt") as file:
			file.read(2)
			pi_number = file.read().replace('\n', '')
	except FileNotFoundError:
		sys.exit("There is no pi.txt file")
	except IsADirectoryError:
		sys.exit("pi.txt is a directory")
	except OSError:
		sys.exit("OSError occurred while reading pi.txt file")

	print("Enter sequence to search for.")
	sequence = input()

	if len(sequence) == 0:
		sys.exit("The sequence must be at least one character long")

	sequences_found = 0
	sequences = []
	current_position = pi_number.find(sequence, 0)
	while current_position != -1:
		if sequences_found < 5:
			sequences.append(str(current_position))

		sequences_found += 1
		current_position = pi_number.find(sequence, current_position + 1)

	print(f'Found {sequences_found} results.')
	if sequences_found > 0:
		print(f'Positions: {" ".join(sequences)} {"..." if sequences_found > 5 else ""}')
