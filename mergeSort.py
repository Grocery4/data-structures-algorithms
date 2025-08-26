# ALGORITHM DESCRIPTION
# separate list into two sublists with two starting indexes: left & right
# compare left and right elements and insert into new array the smallest number.
# continue separating until only two elements remain, then go back in call stack.

import math

# merge both arrays, if one of the arrays is completely analyzed,
# then the remaining elements of the other array are to be added at the end of the merged_array.
def merge(left_array, right_array, array):

    i = 0
    j = 0
    t = 0

    llen = len(left_array)
    rlen = len(right_array)

    while (i<llen and j<rlen):
        if left_array[i] < right_array[j]:
            array[t] = left_array[i]
            i+=1
            t+=1
        else:
            array[t] = right_array[j]
            j+=1
            t+=1



    # remaining elements
    while (i<llen):
        array[t] = left_array[i]
        i+=1
        t+=1
    
    while(j<rlen):
        array[t] = right_array[j]
        j+=1
        t+=1


def mergeSort(lst):
    print(lst)

    length = len(lst)
    if length <= 1:
        return lst

    mid_point = math.ceil(length / 2)
    left_array = mergeSort(lst[0:mid_point])
    right_array = mergeSort(lst[mid_point:length])
    merge(left_array, right_array, lst)
    print('merged: ', lst)
    
    # this was the only thing missing in my code, otherwise everything is fucking working.
    # a whole day to fix this bs.
    return lst

if __name__ == "__main__":
    l = [1,4,2,3,3,0,5,0,2,32,14]
    sorted_l = mergeSort(l)
    print(sorted_l)