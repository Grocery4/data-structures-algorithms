# Heaps are implemented through arrays.
# insertion happens after last leaf left-to-right in the last level of the tree.
# deletion happens by swapping the right-most element in the last level with root node,
# and then popping said root node.

# parent_i = ceil(index/2)-1
# left_i = (2*index) + 1
# right_i = 2*(index+1)

# leaves = [A[floor(n/2 +1)] ; A[n]]

# con un’analisi più accurata:
# “heapify() viene chiamata molte volte su heap bassi,
# poche volte su heap alti” per bubbling delle chiavi
# Costo computazionale O(n)

# https://www.youtube.com/watch?v=pAU21g-jBiE 

from math import floor, ceil

class Heap:
    def __init__(self, array, is_min):
        self.array = array
        self.capacity = len(array)
        self.is_min = is_min

    def getLeftChildIndex(self, index):
        return (2*index)+1
    
    def getRightChildIndex(self, index):
        return 2*(index+1)
    
    def getParentIndex(self, index):
        return (index - 1) // 2

    def swap(self, index_a, index_b):
        self.array[index_a], self.array[index_b] = self.array[index_b], self.array[index_a]

    def bubbleUp(self, index):
        parent_i = ceil((index/2)) - 1
        
        if self.is_min:
            if parent_i >= 0 and self.array[index] < self.array[parent_i]:
                self.swap(index, parent_i)
                self.bubbleUp(parent_i)
        else:
            if parent_i >= 0 and self.array[index] > self.array[parent_i]:
                self.swap(index, parent_i)
                self.bubbleUp(parent_i)

    def heapify(self, index, size):
        left_i = self.getLeftChildIndex(index)        
        right_i = self.getRightChildIndex(index)
        smallest_i = index
        
        if self.is_min:
            if left_i < size and self.array[left_i] < self.array[smallest_i]:
                smallest_i = left_i
            if right_i < size and self.array[right_i] < self.array[smallest_i]:
                smallest_i = right_i

        else:
            if left_i < size and self.array[left_i] > self.array[smallest_i]:
                smallest_i = left_i
            if right_i < size and self.array[right_i] > self.array[smallest_i]:
                smallest_i = right_i

        if smallest_i != index:
            self.swap(smallest_i, index)
            self.heapify(smallest_i, size)

    def insertKey(self, key):
        self.array.append(key)
        self.bubbleUp(len(self.array)-1)
        self.capacity += 1


    def buildHeap(self):
        for i in range((self.capacity // 2) - 1, -1, -1):
            self.heapify(i, self.capacity)

    def getMinimumValue(self):
        return self.array[0]

    def extractMinimumValue(self):
        self.swap(0, (self.capacity-1))
        
        val = self.array.pop(self.capacity-1)
        self.capacity -= 1

        self.buildHeap()
        return val
    
    def heapSort(self):
        self.buildHeap()
        last_i = len(self.array)-1

        for end in range(last_i, -1,-1):
            self.swap(0, end)
            self.heapify(0, end)

    def __str__(self):
        if not self.array:
            return "<empty heap>"

        n = len(self.array)
        height = n.bit_length()  # number of levels
        lines = []

        index = 0
        for level in range(height):
            level_size = 2 ** level
            level_nodes = self.array[index:index + level_size]

            # spacing logic
            spaces_before = " " * ((2 ** (height - level - 1)) - 1)
            spaces_between = " " * ((2 ** (height - level)) - 1)

            line = spaces_before + spaces_between.join(str(x) for x in level_nodes)
            lines.append(line)

            index += level_size
            if index >= n:
                break

        return "\n".join(lines)


if __name__ == '__main__':
    initial_array = [30,19,12,16,2,9,7,3,8,10]
    h = Heap(initial_array, False)
    # print(h)
    h.bubbleUp(4)

    h.buildHeap()
    # print(h)

    h.insertKey(15)
    h.insertKey(6)
    h.insertKey(1)

    # print(h)
    h.extractMinimumValue()
    # print(h)

    initial_array = [1,6,17,21,2,4,3,9,0,5,23,8,24]
    heap = Heap(initial_array, False)
    print('unsorted:\n',heap)
    heap.heapSort()
    print('sorted:\n',heap)