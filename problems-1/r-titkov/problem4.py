def print_song_text():
	int_to_str = {
		0: 'No', 1: 'One', 2: 'Two', 3: 'Three', 
		4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 
		8: 'Eight', 9: 'Nine', 10: 'Ten'
	}
	wall = 'hanging on the wall'
	bottle = 'bottle'
	green = 'green'

	for count in range(10, 0, -1):
		for _ in range(2):
			print(f'{int_to_str[count]} {green} {bottle}{"" if count == 1 else "s"} {wall}')

		print(f'And if one {green} {bottle} should accidentally fall,')
		print(f'There’ll be {int_to_str[count - 1].lower()} {green} {bottle}s {wall}.')

if __name__ == '__main__':
	print_song_text()
