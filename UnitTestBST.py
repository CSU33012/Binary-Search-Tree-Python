import unittest
import BST

class Testing(unittest.TestCase):

    def test_basic_LCA(self):
        root = BST.Node(1)                                  
        root.left = BST.Node(2) 
        root.right = BST.Node(3) 
        root.left.left = BST.Node(4) 
        root.left.right = BST.Node(5) 
        root.right.left = BST.Node(6) 
        root.right.right = BST.Node(7) 
        self.assertEqual(BST.findLCA(root, 2, 3), 1)
        
    def test_complex_LCA(self):
        root = BST.Node(1)
        root.left = BST.Node(2) 
        root.right = BST.Node(3) 
        root.left.left = BST.Node(4) 
        root.left.right = BST.Node(5) 
        root.right.left = BST.Node(6) 
        root.right.right = BST.Node(7) 
        self.assertEqual(BST.findLCA(root, 4, 5), 2)
        
    def test_empty_tree_LCA(self):
        root = BST.Node(1)
        self.assertEqual(BST.findLCA(root, 2, 3), -1)
        

if __name__ == '__main__':
    unittest.main()
