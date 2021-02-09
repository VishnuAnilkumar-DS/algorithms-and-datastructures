"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in
 wrong order.
"""


class BubbleSort:

    def __init__(self, nums):
        self.nums = nums

    def sort(self):

        for i in range(len(self.nums)-1):
            for j in range(len(self.nums)-i-1):
                if self.nums[j] < self.nums[j+1]:
                    self.swap(j, j+1)

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]


if __name__ == '__main__':

    n = [9, -96, 0, 2, -1, 6, 9, 55, 56, -62]
    bubble_sort = BubbleSort(n)
    bubble_sort.sort()
    print(bubble_sort.nums)
