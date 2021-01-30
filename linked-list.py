class Node(object):
    """ Definition of a basic node for a Linkedlist. """

    def __init__(self, data):
        self.data = data  # store the data
        self.nextNode = None  # store the reference to the nextnode


class LinkedList(object):
    """ Definition for a linked list obj. """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  # initialize the size of the head an the list

    def insert_at_start(self, data):
        """ Inserts a node at the start of a LinkedList. """

        self.size = self.size + 1  # increment the size of the list
        newNode = Node(data)  # instantiate a new node

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head  # The newnode now points to the head
            self.head = newNode

    def size(self):
        """ Returns the size of a node.
        Constant time complexity : O(1)"""
        return self.size

    def size2(self):
        """iterates through the list and returns the size (01^)"""

        currentNode = self.head
        size = 0

        while currentNode is not None:
            size += 1
            currentNode = currentNode.nextNode

        return size

    def insert_end(self, data):
        """ iterates through the linked list and add a node to the end"""

        self.size = self.size + 1
        newNode = Node(data)  # instantiate a new node with the data
        currentNode = self.head

        while currentNode.nextNode is not None:
            # Traverse in the whole list
            currentNode = currentNode.nextNode

        currentNode.nextNode = newNode

    def traverse_list(self):
        """Iterates through the entire list
        O(N) - Linear time complexity"""
        currentNode = self.head

        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode

    def remove(self, data):
        if self.head is None:
            return
        actual_node = self.head
        previous_node = None
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = previous_node.nextNode
        self.size = self.size - 1
        if actual_node is None:
            # search miss
            return
        if previous_node is None:
            self.head = actual_node.nextNode
        else:
            previous_node.nextNode = actual_node.nextNode
        print(data, " has removed")


LinkedList = LinkedList()

LinkedList.insert_at_start(19)
LinkedList.insert_at_start(31)
LinkedList.insert_at_start(90)
LinkedList.insert_end(96)
LinkedList.insert_at_start(300)
LinkedList.traverse_list()
LinkedList.remove(90)
