CAPACITY = 10


class Heap(object):
    def __init__(self):
        # create an array slot as same as the size of CAPACITY
        self.heap = [0] * CAPACITY
        self.heap_size = 0

    def insertion(self, item):
        #         insertion takes O(1) running time but we have to make sure that the heap properties are not violated
        #          (it takes O(logN) because fixup() method
        if self.heap_size == CAPACITY:
            # cannot insert more items than CAPACITY value
            return
        # Insert and increment the counter
        self.heap[self.heap_size] = item
        self.heap_size = self.heap_size + 1
        #         inorder fix the heap issue while inserting in the end we use a fix_up() function
        self.fix_up(self.heap_size - 1)

    def fix_up(self, index):
        # running time : O(N)
        # Consider the last item and checks whether swapping is necessary
        parent_index = (index - 1) // 2

        #         index > 0 means until we consider all the items "above " the one we inserted
        # we have to swap if heap property is violated ie largest item in the root (max item ===root node)
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.swap(index, parent_index)
            self.fix_up(parent_index)

    def get_max(self):
        # peek
        #  running time O(N)
        #             Return default root node
        return self.heap[0]

    def poll(self):
        # O(logN)
        max = self.get_max()
        self.swap(0, self.heap_size - 1)
        self.fix_down(0)
        return max

    def fix_down(self, index):
        # every node has left and right children
        # node i in an array has left child with index *i+1 and right child with index 2*1+1
        index_left = 2 * index + 1
        index_right = 2 * index + 2
        index_largest = index
        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            # if left child i greater than parent then largest is left node
            index_largest = index_left
        if index_right < self.heap_size and self.heap[index_right] > self.heap[index_largest]:
            # If right child is greater than left child : largest is the right node
            index_largest = index_right
        if index != index_largest:
            self.swap(index, index_largest)
            # we do not want to swap item with themselves
            self.fix_down(index_largest)

    def heap_sort(self):
        size = self.heap_size
        for i in range(0, size):
            max = self.poll()
            print(max)
        
    def swap(self, index1, index2):
        # swap to items in with index1 and index2 in the heap array
        self.heap[index2], self.heap[index1] = self.heap[index1], self.heap[index2]


if __name__ == "__main__":
    heap = Heap()
    heap.insertion(10)
    heap.insertion(8)
    heap.insertion(12)
    heap.insertion(20)
    heap.insertion(-2)
    heap.insertion(0)
    heap.insertion(1)
    heap.insertion(321)
    heap.heap_sort()
