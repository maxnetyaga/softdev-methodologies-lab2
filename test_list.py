#!/usr/bin/env python
import unittest as u
from list import List


class TestList(u.TestCase):
    def setUp(self):
        self.list1 = List("H", "e", "l", "l", "o", ",", " ",
                          "w", "o", "r", "l", "d", "!")

    def test_length(self):
        self.assertEqual(self.list1.length(), 13)

    def test_get(self):
        ...

    def test_append(self):
        ...

    def test_extend(self):
        ...

    def test_delete(self):
        ...

    def test_deleteAll(self):
        ...

    def test_clone(self):
        ...

    def test_reverse(self):
        ...

    def test_findFirst(self):
        ...

    def test_findLast(self):
        ...

    def test_clear(self):
        ...


if __name__ == '__main__':
    u.main()
