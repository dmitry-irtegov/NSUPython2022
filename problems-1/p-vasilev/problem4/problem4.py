#!/usr/bin/env python3

num_to_str_dict = {
    0: 'no',
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}


def num_to_bottles(n: int):
    """Converts a number to a string about bottles."""
    return f'{num_to_str_dict[n]} green bottle{"s" if n != 1 else ""}'


def main():
    start_num = 10
    end_num = 0
    step = 1
    hang_str = 'hanging on the wall'
    for i in range(start_num, end_num, -step):
        for j in range(2):
            print(f'{num_to_bottles(i).capitalize()} {hang_str},')

        print(f"{'If that' if i == 1 else 'And if'} {num_to_bottles(step)} should accidentally fall")

        print(f'There’ll be {num_to_bottles(i - step)} {hang_str}.')


if __name__ == '__main__':
    main()
