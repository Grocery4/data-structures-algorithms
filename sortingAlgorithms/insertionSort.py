# ALGORITHM DESCRIPTION
# Start from 1 element in 'hand'
# Iterate each element of list and insert into 'hand'
# To insert element in 'hand' compare new_insert to each element of the sublist
# if element is not in its place, keep switching as if it were a bubble(?)

def insertSort(lst):
    # `hand` sublist could be initialized with one element already to avoid 1 pass in while-loop.
    # works with range(0,n) too.
    for analyzed_index in range(0,len(lst)):
        
        hand_sublist_index = analyzed_index-1
        tmp = lst[analyzed_index]
        print(tmp)
        
        # save the element to place into a temporary variable `tmp`
        # and each element which gets visited gets placed into `tmp`'s index
        # until tmp gets placed into its right index and the element which got evicted
        # takes `tmp`'s old index.

        while (hand_sublist_index>=0 and lst[hand_sublist_index] > tmp):
            lst[hand_sublist_index+1] = lst[hand_sublist_index]
            hand_sublist_index-=1
        lst[hand_sublist_index+1] = tmp

l = [1,4,2,3,3,0,5,0,2,32,14]
insertSort(l)
print(l)