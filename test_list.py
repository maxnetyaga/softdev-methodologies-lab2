#!/usr/bin/env python
from re import L
import unittest as u
from list import List


class TestList(u.TestCase):
    def setUp(self):
        self.list1 = List("H", "e", "l", "l", "o", ",", " ",
                          "w", "o", "r", "l", "d", "!")

    def test_str(self):
        self.assertEqual("Hello, world!", str(self.list1))

    def test_length(self):
        self.assertEqual(self.list1.length(), 13)

    def test_get(self):
        self.assertEqual(self.list1.get(0), "H")
        self.assertEqual(self.list1.get(12), "!")

    def test_get_exceptions(self):
        with self.assertRaises(IndexError):
            self.list1.get(-1)
        with self.assertRaises(IndexError):
            self.list1.get(13)

    def test_append(self):
        with self.assertRaises(ValueError):
            self.list1.append("word")

        self.list1.append("M")
        self.assertEqual(self.list1.length(), 14)
        self.assertEqual(self.list1.get(13), "M")

    def test_extend(self):
        list2 = List(" ", "B", "y", "e", "!")
        self.list1.extend(list2)

        self.assertEqual(self.list1.length(), 18)
        self.assertEqual(self.list1.get(17), "!")
        self.assertEqual(self.list1.get(13), " ")

    def test_delete(self):
        self.list1.delete(0)
        self.list1.delete(11)

        self.assertEqual(self.list1.length(), 11)
        self.assertEqual(self.list1.get(0), "e")
        self.assertEqual(self.list1.get(10), "d")

    def test_delete_exceptions(self):
        with self.assertRaises(IndexError):
            self.list1.delete(-1)
        with self.assertRaises(IndexError):
            self.list1.delete(20)

    def test_deleteAll(self):
        self.list1.delete_all("l")

        self.assertEqual(str(self.list1), "Heo, word!")
        with self.assertRaises(ValueError):
            self.list1.delete_all("DH")

    def test_clone(self):
        list2 = self.list1.clone()

        self.assertTrue(self.list1 == list2)

        self.assertEqual(self.list1.length(), list2.length())
        self.assertNotEqual(id(self.list1), id(list2))
        self.assertFalse(self.list1._get_node(5) is list2._get_node(5))


    def test_reverse_order(self):
        self.list1.reverse()

        for i in range(self.list1.length()):
            self.assertEqual(str(self.list1)[::-1], "Hello, world!")
            
    def test_reverse_id(self):
        list1_initial_id = id(self.list1)
        self.list1.reverse()
        list1_reversed_id = id(self.list1)

        self.assertEqual(list1_initial_id, list1_reversed_id)

    def test_findFirst(self):
        first_l_index = self.list1.find_first("l")

        self.assertEqual(first_l_index, 2)
        self.assertEqual(self.list1.find_first("x"), -1)

    def test_findLast(self):
        first_l_index = self.list1.find_last("l")

        self.assertEqual(first_l_index, 10)
        self.assertEqual(self.list1.find_first("x"), -1)

    def test_clear(self):
        self.list1.clear()

        self.assertEqual(self.list1.length(), 0)


if __name__ == '__main__':
    u.main()
