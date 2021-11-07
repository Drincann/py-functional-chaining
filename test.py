import unittest
from funcChaining.Type import List


class ListTest(unittest.TestCase):
    def setUp(self) -> None:

        self.lst = List(range(1, 5))

    def test_pack(self):
        try:
            self.lst.__class__.pack([])
        except NotImplementedError:
            self.assertTrue(False, 'pack 没有被实现')

    def test_map(self):
        self.assertEqual(self.lst.map(lambda x: x * 2), [2, 4, 6, 8])

    def test_filter(self):
        self.assertEqual(self.lst.filter(lambda x: x % 2 == 0), [2, 4])

    def test_reduce(self):
        self.assertEqual(self.lst.reduce(lambda x, y: x + y, initial=0), 10)

    def test_zip(self):
        self.assertEqual(self.lst.zip(range(1, 5)), [
                         (1, 1), (2, 2), (3, 3), (4, 4)])

    def test_clear(self):
        self.lst.clear()
        self.assertEqual(self.lst, [])

    def test_insert(self):
        self.lst.insert(0, 0)
        self.assertEqual(self.lst, [0, 1, 2, 3, 4])

    def test_append(self):
        self.lst.append(5)
        self.assertEqual(self.lst, [1, 2, 3, 4, 5])

    def test_pop(self):
        self.assertEqual(self.lst.pop(), self.lst)
        self.assertEqual(self.lst, [1, 2, 3])

    def test_extend(self):
        self.lst.extend([5])
        self.assertEqual(self.lst, [1, 2, 3, 4, 5])

    def test_remove(self):
        self.lst.remove(2)
        self.assertEqual(self.lst, [1, 3, 4])

    def test_reverse(self):
        self.assertEqual(self.lst.reverse(), [4, 3, 2, 1])

    def test_sort(self):
        self.assertEqual(self.lst.sort(key=lambda x: -x), [4, 3, 2, 1])

    def test_copy(self):
        newlst = self.lst.copy()
        newlst[0] = 0
        self.assertEqual(self.lst, [1, 2, 3, 4])
        self.assertEqual(newlst, [0, 2, 3, 4])

    def test_index(self):
        self.assertEqual(self.lst.index(3), 2)

    def test_count(self):
        self.assertEqual(self.lst.count(3), 1)


if __name__ == "__main__":
    unittest.main()
