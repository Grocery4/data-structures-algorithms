# ALGORITHM DESCRIPTION
# get pivot and move to end of array
# compare elements from left and right:
#   lefts > pivot and rights <= pivot should swap

from math import floor


def partition(lst, low_i, high_i, pivot_i):
    # swap pivot to last place of array
    lst[pivot_i], lst[high_i] = lst[high_i], lst[pivot_i]

    # my error was here! separator index should start ONE LESS low_index
    # and should not be initialized to -1, as in subsequent
    # recursive calls, low_index could be != 0
    separator_i = low_i -1
    # for does not include upper bound, no need to -1 it!
    # move elements <= pivot left of separator
    for index in range(low_i, high_i):
        if lst[index] <= lst[high_i]:
            separator_i +=1
            lst[separator_i], lst[index] = lst[index], lst[separator_i]

    # swap pivot to its place and return its index for quicksort recursion
    lst[high_i], lst[separator_i+1] = lst[separator_i+1], lst[high_i]

    # return pivot locked in position
    return separator_i+1

def quickSort(lst, low_i, high_i):
    # base case: one or 0 elements in lst
    if (high_i <= low_i):
        return

    pivot_i = floor((low_i+high_i)/2)
    print('pivot index:',pivot_i, lst)
    
    sorted_i = partition(lst, low_i, high_i, pivot_i)
    print('locked index:',sorted_i, lst)
    
    # left quickSort
    quickSort(lst, low_i, sorted_i-1)
    # right quickSort
    quickSort(lst, sorted_i+1, high_i)

l = [6, 1, 4, 3, 0, 14, 0, 1, 3]
quickSort(l, 0, len(l)-1)
print(l)