# ALGORITHM DESCRIPTION
# - build heap
# - swap first and last elements
# - lock last element
# - heapify
# - repeat from line3

from heap import Heap

def heapSort(heap: "Heap"):
    heap.buildHeap()
    last_i = len(heap.array)-1

    for end in range(last_i, -1,-1):
        heap.swap(0, end)
        heap.heapify(0, end)

        input()



initial_array = [1,6,17,21,2,4,3,9,0,5,23,8,24]
heap = Heap(initial_array, False)
print('unsorted:\n',heap)
heapSort(heap)
print('sorted:\n',heap)