import unittest
import LCAPython
from LCAPython import Node

class PythonTests(unittest.TestCase):
    def setUp(self): 
        pass

    LCAPython.root = LCAPython.Node(1)
    LCAPython.root.left = LCAPython.Node(2)
    LCAPython.root.right = LCAPython.Node(3)
    LCAPython.root.left.left = LCAPython.Node(4)
    LCAPython.root.left.right = LCAPython.Node(5)
    LCAPython.root.right.left = LCAPython.Node(6)
    LCAPython.root.right.right = LCAPython.Node(7)
    LCAPython.root.left.right.left = LCAPython.Node(8)
    LCAPython.root.left.right.right = LCAPython.Node(9)
    LCAPython.root.right.right.left = LCAPython.Node(10)
    LCAPython.root.right.right.right = LCAPython.Node(11)
    LCAPython.root.left.right.right.left = LCAPython.Node(12)
    LCAPython.root.left.right.right.right = LCAPython.Node(13)

    def test1(self):
        self.assertEqual(LCAPython.LCA(6,10), 3)

    def test2(self):
        self.assertEqual(LCAPython.LCA(8,9), 5)

    def test3(self):
        self.assertEqual(LCAPython.LCA(7,11), 7)

    def test2(self):
        self.assertEqual(LCAPython.LCA(12,3), 1)

if __name__ == '__main__': 
    unittest.main()