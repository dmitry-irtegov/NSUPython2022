import argparse
import sys
import unittest
from .tr_impl import translate


class TranslateTests(unittest.TestCase):
    @staticmethod
    def non_lazy_tr(*args):
        return "".join(translate(*args))

    def test_sanity(self):
        test_string = 'hello world'
        self.assertEqual(
            test_string, TranslateTests.non_lazy_tr(test_string, dict()))

    def test_translage(self):
        test_string = 'hello world'
        mapping = {' ': '_'}
        expected = 'hello_world'
        self.assertEqual(
            expected, TranslateTests.non_lazy_tr(test_string, mapping))

    def test_deletion(self):
        test_string = "     w  h i    t e s pa c e          "
        to_delete = set('   ')
        expected = "whitespace"
        self.assertEqual(expected, TranslateTests.non_lazy_tr(
            test_string, dict(), to_delete))

    def test_delete_before_change(self):
        test_string = "hotdog"
        to_delete = set("o")
        mapping = {'o': 'b'}
        expected = "htdg"
        self.assertEqual(expected, TranslateTests.non_lazy_tr(
            test_string, mapping, to_delete))


class ArgsAssertionTest(unittest.TestCase):
    def test_args_good(self):
        frm = 'abc'
        to = 'ijk'
        assert_good_args(frm, to)
    
    def test_args_bad_length(self):
        longer = 'abcdef'
        shorter = 'zx'
        with self.assertRaises(ArgsLengthError):
            assert_good_args(longer, shorter)
        with self.assertRaises(ArgsLengthError):
            assert_good_args(shorter, longer)
    
    def test_args_bad_map(self):
        frm = 'abcdefa'
        to = 'x' * len(frm)
        with self.assertRaises(ArgsDoubleMapError):
            assert_good_args(frm, to)

    def test_double_map_char(self):
        frm = 'abcda'
        to = 'x' * len(frm)
        try:
            assert_good_args(frm, to)
            self.fail()
        except ArgsDoubleMapError as e:
            self.assertEqual('a', e.doubled_chr)

def run_tests():
    sys.argv = [x for x in sys.argv if x != '--run-tests']
    unittest.main()


class TestsAction(argparse.Action):
    def __init__(self, option_strings, dest, **kwargs):
        return super().__init__(option_strings, dest, nargs=0, default=argparse.SUPPRESS, **kwargs)

    def __call__(self, parser, namespace, values, option_string, **kwargs):
        run_tests()
        sys.exit(0)

class ArgsLengthError(ValueError):
    pass

class ArgsDoubleMapError(ValueError):
    def __init__(self, doubled_chr):
        self.doubled_chr = doubled_chr

def assert_good_args(frm, to):
    if len(frm) != len(to):
        raise ArgsLengthError()
    frm_set = set()
    for frm_chr in frm:
        if frm_chr in frm_set:
            raise ArgsDoubleMapError(frm_chr)
        frm_set.add(frm_chr)


def main():
    try:
        parser = argparse.ArgumentParser(
            prog='tr', description='Translate stdin using a dictionary')
        parser.add_argument(
            'frm', type=str, help='Characters you want to change in the source')
        parser.add_argument(
            'to', type=str, help='Characters you want to see after the change')
        parser.add_argument('-d', '--delete', type=str,
                            help='Characters you want to delete from the input')
        parser.add_argument(
            '--run-tests', help='Run tests instead of running the program', action=TestsAction)
        args = parser.parse_args()
        assert_good_args(args.frm, args.to)
        iterable_stdin = iter(lambda: sys.stdin.read(1), '')
        result = translate(iterable_stdin, dict(zip(args.frm, args.to)), set(
            args.delete) if args.delete is not None else None)
        for x in result:
            print(x, end='')
    except ArgsLengthError:
        print("Error: Lengths of supplied FRM and TO are not equal", file=sys.stderr)
        sys.exit(1)
    except ArgsDoubleMapError as e:
        print(
            f"Error: FRM contains one letter twice: {e.doubled_chr}", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(
            f"Error: unexpected error during execution: {e}", file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    main()
