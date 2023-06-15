import unittest
from utils import arrs


class TestArrs(unittest.TestCase):
    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "Array is empty")
        self.assertEqual(arrs.get([1, 2, 3], -1, "out of range"), "out of range")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([], 0), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -4), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
