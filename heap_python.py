from heapq import heappop, heapify, heappush

heap = []
nums = [12, 3, 20,-2, 35, 5, 66]

for num in nums:
    heappush(heap, num)

while heap:
    print(heap.pop())

heapify(nums)
print(nums)
