import unittest


def pythagorean_triples(n):
    """
    pythagorean triples where every component is not greater than n
    :param n: number to limit size of components of pythagorean triples
    :returns: list of (x,y,z), where (x,y,z) is pythagorean triple with each component
    not greater then n. Every (x,y,z) is sorted ascending
    """
    return [
        (x, y, z)
        for x in range(1, n + 1)
        for y in range(x, n + 1)
        for z in range(y, n + 1)
        if x * x + y * y == z * z
    ]


class TestPrimeFactors(unittest.TestCase):

    def test_simple_cases(self):
        self.maxDiff = None
        self.assertCountEqual(pythagorean_triples(5), [(3, 4, 5)])
        self.assertCountEqual(pythagorean_triples(10), [(3, 4, 5), (6, 8, 10)])
        self.assertCountEqual(pythagorean_triples(11), [(3, 4, 5), (6, 8, 10)])
        self.assertCountEqual(pythagorean_triples(13), [(3, 4, 5), (6, 8, 10), (5, 12, 13)])

        primitive_triangles = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
                               (20, 21, 29), (12, 35, 37), (9, 40, 41), (28, 45, 53),
                               (11, 60, 61), (16, 63, 65), (33, 56, 65), (48, 55, 73),
                               (13, 84, 85), (36, 77, 85), (39, 80, 89), (65, 72, 97)]

        self.assertSetEqual(set(pythagorean_triples(100)).intersection(primitive_triangles), set(primitive_triangles))

    def test_sizes_of_specific_num(self):
        # A009003 sequence
        arr = [5, 10, 13, 15, 17, 20]
        for i in range(len(arr)):
            self.assertEqual(len(pythagorean_triples(arr[i])), i + 1)


if __name__ == '__main__':
    unittest.main()
