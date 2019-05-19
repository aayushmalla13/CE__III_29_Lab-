import unittest
from BinarySearchTree import BST

class BSTTestCase(unittest.TestCase):
	def testBinarySearch(self):
		bst = BST()

		bst.addNode(10, "Value 1")
		self.assertEqual(bst.size(),1)

		bst.addNode(5, "Value 2")
		self.assertEqual(bst.size(),2)

		bst.addNode(30, "Value 2")
		self.assertEqual(bst.size(),3)

		self.assertListEqual(bst.inOrderTraverse(), [15, 20, 30])
		self.assertListEqual(bst.preOrderTraverse(), [20, 15, 30])
		self.assertListEqual(bst.postOrderTraverse(), [15, 30, 20])

		self.assertListEqual(bst.searchSmallestKey(), 5)
		self.assertListEqual(bst.searchLargestKey(), [30])

		self.assertEqual(bst.searchForNode(10), [1])

if __name__  == '__main__':
	unittest.main()