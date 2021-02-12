class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = parent


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    # O(logN) BUT if the tree is balances (left subtree contains app. same amount of item then right subtree)
    def insert_node(self, data, node):

        # we have to go to the left subtree
        if data < node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data, node)
        # we have to visit the right subtree
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data, node)

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):

        if node.left_child:
            self.traverse_in_order(node.left_child)

        print('%s' % node.data)

        if node.right_child:
            self.traverse_in_order(node.right_child)

    def get_max(self, node):
        #  In binary search tree right most value will be the largest value
        if node.right_child:
            return self.get_max(node.right_child)
        return node.data
    
    # Getting max without recursion
    # def get_max(self, node):
    #     # Max without recursion
    #     actual = self.root
    #     while actual.right_child is not none:
    #         actual = actual.right_child
    #     return actual.data

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_min(self, node):
        #  In binary search tree left most value will be the smallest value
        if node.left_child:
            return self.get_min(node.left_child)
        return node.data

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(66)
bst.traverse()
print("MAX ITEM IS: ", bst.get_max(bst.root))
print("MIN ITEM IS: ", bst.get_min(bst.root))
