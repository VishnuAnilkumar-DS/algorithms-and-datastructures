class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def bread_first_search(start_node):
    # FIFO
    queue = [start_node]
    while queue:
        # Remove and return 1st item we inserted to list
        actual_node = queue.pop()
        print(actual_node.name)

        # Considering neighbour nodes one by one
        for n in actual_node.adjacency_list:
            # if not visited append
            if not n.visited:
                queue.append(n)


if __name__ == '__main__':
    # Create node or vertices
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    # Handling neighbours
    node1.adjacency_list.append(node2)
    node2.adjacency_list.append(node3)
    node3.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)
    # RUN BFS
    bread_first_search(node1)
