# i didnt even know tiebreakers were a thing, there's no tiebreakers in the slides.


from dataStructures.trees_perfect import PerfectTree
from queue import PriorityQueue

import itertools

counter = itertools.count()



class Node:
    def __init__(self, character, frequency, parent=None, left=None, right=None):
        self.character = character
        self.frequency = frequency
        self.parent = parent
        self.left = left
        self.right = right

    
    def __lt__(self, other):
        return self.character < other.character

    def __str__(self):
        def _build_str(node, indent=0):
            if node is None:
                return ""
            result = " " * indent + f"{node.character}:{node.frequency}\n"
            result += _build_str(node.left, indent + 4)
            result += _build_str(node.right, indent + 4)
            return result

        return _build_str(self)    
    
    
def generate_codes(node, prefix="", codes=None):
    if codes is None:
        codes = {}
    if node is None:
        return codes
    if node.left is None and node.right is None:  # leaf
        codes[node.character] = prefix or "0"
    else:
        generate_codes(node.left, prefix + "0", codes)
        generate_codes(node.right, prefix + "1", codes)
    return codes

    # def __repr__(self):
    #     return f'{self.character}'

def huffman(frequency):
     
    pq = PriorityQueue()

    for char, freq in frequency.items():
        node = Node(char, freq)
        pq.put((freq, next(counter), node))

    while len(pq.queue) >= 2:
        lowest_freq1 = pq.get()
        lowest_freq2 = pq.get()
        
        new_freq = lowest_freq1[0]+lowest_freq2[0]
        new_node = Node('-', new_freq, None, lowest_freq1[2], lowest_freq2[2])
        lowest_freq1[2].parent = new_node
        lowest_freq2[2].parent = new_node
        
        pq.put((new_freq, next(counter), new_node))
    
    return pq.get()[2]


if __name__ == '__main__':
    string = 'adwafgwadwa'
    c_frequency = {char:0 for char in string}

    for char in string:
        c_frequency[char] += 1


    huffman_tree = huffman(c_frequency)
    print(huffman_tree)
    codes = generate_codes(huffman_tree)

    result = ''
    for char in string:
        result += codes[char]

    print(codes)
    print(result)