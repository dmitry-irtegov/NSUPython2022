import unittest
from collections import defaultdict, OrderedDict


def inverse_dict(d):
    if type(d) is not dict:
        raise TypeError("You must provide a dict")
    answer = defaultdict(list)
    for k, v in d.items():
        if type(v) is not list:
            raise TypeError("All values of a dict must be list of smth")
        for word in v:
            answer[word].append(k)

    return OrderedDict(sorted(answer.items(), key=lambda item: item[0], reverse=False))


class TestDictInv(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(inverse_dict({"apple": ["malum", "pomum", "popula"],
                                       "fruit": ["baca", "bacca", "popum"],
                                       "punishment": ["malum", "multa"]}),
                         OrderedDict([
                             ("baca", ["fruit"]),
                             ("bacca", ["fruit"]),
                             ("malum", ["apple", "punishment"]),
                             ("multa", ["punishment"]),
                             ("pomum", ["apple"]),
                             ("popula", ["apple"]),
                             ("popum", ["fruit"])
                         ]))

        self.assertEqual(inverse_dict({}), OrderedDict())
        self.assertEqual(inverse_dict({"b": ["a"], "a": ["b"]}), OrderedDict([("a", ["b"]), ("b", ["a"])]))

    def test_error(self):
        self.assertRaises(TypeError, inverse_dict, None)
        self.assertRaises(TypeError, inverse_dict, 3)
        self.assertRaises(TypeError, inverse_dict, "sad")
        self.assertRaises(TypeError, inverse_dict, [1, 2, 3])
        self.assertRaises(TypeError, inverse_dict, {"f": [1, 2, 3], "b": "C"})
        
