import argparse
import sys
from problem2_impl import inverse_dict


def parse_dict(s):
    lines = s.splitlines()
    dict = {}
    for line in lines:
        if len(line.split("-")) != 2:
            raise ValueError("All lines in a dict must be like 'word - word1, word2, word3'")
        f, t = line.split("-")
        f = f.strip()
        words = [word.strip() for word in t.split(",")]
        if not f.isalpha() \
                or not all(map(lambda x: x.strip().isalpha(), words)):
            raise ValueError("All words must be represented only by a-zA-Z characters")
        dict[f] = [word.strip() for word in t.split(",")]
    return dict


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("path", help="path to dictionary", type=str)
    args = p.parse_args()
    file_path = args.path
    try:
        with open(file_path, "r") as f:
            d = parse_dict(f.read())
            for key, values in inverse_dict(d).items():
                print(key, " - ", ", ".join(values))

    except OSError as e:
        print(f"Error occurred while reading a file {file_path}", file=sys.stderr)
        exit(1)

    except ValueError as e:
        print(e, file=sys.stderr)
        exit(1)

    except Exception as e:
        print(f"Unexpected error occurred", file=sys.stderr)
        print(e, file=sys.stderr)
        exit(1)
