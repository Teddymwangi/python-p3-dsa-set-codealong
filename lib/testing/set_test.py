import unittest
from MySet import MySet

class TestMySet(unittest.TestCase):
    def test_init(self):
        my_set = MySet([1, 2, 3, 3])
        self.assertEqual(str(my_set), "MySet: {1,2,3}")

    def test_has(self):
        my_set = MySet([1, 2, 3])
        self.assertTrue(my_set.has(2))
        self.assertFalse(my_set.has(4))

    def test_add(self):
        my_set = MySet([1, 2, 3])
        my_set.add(4)
        self.assertTrue(my_set.has(4))
        self.assertEqual(str(my_set), "MySet: {1,2,3,4}")

    def test_delete(self):
        my_set = MySet([1, 2, 3])
        my_set.delete(2)
        self.assertFalse(my_set.has(2))
        self.assertEqual(str(my_set), "MySet: {1,3}")

    def test_size(self):
        my_set = MySet([1, 2, 3])
        self.assertEqual(my_set.size(), 3)

    def test_clear(self):
        my_set = MySet([1, 2, 3])
        my_set.clear()
        self.assertEqual(str(my_set), "MySet: {}")

if __name__ == '__main__':
    unittest.main()
