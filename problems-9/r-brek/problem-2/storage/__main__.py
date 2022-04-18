from .storage_impl import Storage
from time import sleep
import unittest


class StorageTest(unittest.TestCase):
    def test_sanity(self):
        storage = Storage()
        self.assertEqual(0, len(storage))
        with storage.edit() as transaction:
            transaction[0] = 1
            transaction[1] = 2
            transaction[2] = 3
        self.assertEqual(3, len(storage))

    def test_setting_no_transaction(self):
        with self.assertRaises(ValueError):
            storage = Storage()
            storage["key"] = "value"

    def test_transaction_failure(self):
        storage = Storage({1: 1})
        try:
            with storage.edit() as transaction:
                transaction[1] = 0
                raise ValueError()
        except ValueError as e:
            pass
        self.assertEqual(1, storage[1])

    def test_transaction_no_failure(self):
        storage = Storage({1: 1})
        try:
            with storage.edit() as transaction:
                transaction[1] = 0
        except ValueError as e:
            pass
        self.assertEqual(0, storage[1])

    def test_keys(self):
        storage = Storage({1: 1, 2: 2, 3: 3})
        keys = list(storage.keys())
        self.assertEqual([1, 2, 3], keys)

    def test_get_in_transaction(self):
        storage = Storage()
        with storage.edit() as transaction:
            transaction['key'] = 'value'
            self.assertEqual('value', transaction['key'])
        self.assertEqual('value', storage['key'])

if __name__ == "__main__":
    unittest.main()
