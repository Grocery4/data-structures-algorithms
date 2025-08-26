# ALGORITHM DESCRIPTION
# \*stable: if multiple instances of an object exist, say: '2'
# and we give them a name: 2_a, 2_b, 2_c,
# in the array we'd have:
# [0, 2_c, 3, 4, 2_a, 6, 1, 2_b]
# in the unstable version of countingSort we'd have:
# ... 2_b, 2_a, 2_c ...
#  whereas in the stable version you'd have the correct order of appearance: 
# ... 2_c, 2_a, 2_b ...

# the difference between stable and unstable is that the order of
# traversing the array is from last to first (stable) instead of first to last (unstable)

# - define what the max. value of element in array Array[] is
# - count each occurance of element in array through a supporting array Count[]
# - go through the Array[] in reverse order
# - Count[element]-1 is the sorted position in array
# - after placing element in array decrease Count[element]

def countSort(lst, max_value):
    result = [None for _ in range(len(lst))]
    # create count_array
    count_array = [0 for _ in range(max_value+1)]

    # populate count_array
    for element in lst:
        count_array[element] += 1

    # cumulative sum
    for i in range(1,len(count_array)):
        count_array[i] += count_array[i-1]

    # populate result array
    for i in range(len(lst)-1,-1,-1):
        result[count_array[lst[i]]-1] = lst[i]
        count_array[lst[i]] -= 1
    
    return result

l = [6, 1, 4, 3, 0, 10, 0, 1, 3]
sorted_l = countSort(l, 10)
print(sorted_l)
