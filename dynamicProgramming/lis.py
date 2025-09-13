def lis(j, A):
    # if one element only then max_length is 1
    if j == 0:
        return 1
    
    # - iterate each element up until j
    # - recursively do so for any element < A[j]
    # - the function simply iterates on each element and seeks the longest path, keeping track
    #   exclusively of max_length, and excluding the actual path it takes.

    # the algorithm calculates each path to j and keeps the most advantageous one (longest path = max)
    max_length = 0
    for i in range(0, j):
        if A[i] < A[j]:
            length_i = lis(i, A)
            print(f'{A[i]=}, {length_i=}')
            
            if length_i > max_length:
                max_length = length_i
    return max_length + 1

def lisWithSubsequence(j, A, subseq):
    # if one element only then max_length is 1
    if j == 0:
        subseq.append(A[j])
        return 1, subseq
    
    max_length = 0
    for i in range(0, j):
        tmp_subseq = []
        if A[i] < A[j]:
            length_i, ss = lis(i, A)
            tmp_subseq.append(ss)
            print(f'{A[i]=}, {length_i=}')
            
            if length_i > max_length:
                max_length = length_i
    return max_length + 1

import bisect

def longest_increasing_subsequence(nums):
    if not nums:
        return []
    
    # tails[i] stores the smallest tail of all increasing subsequences of length i+1
    tails = []
    # prev[i] stores the index of the previous element in the LIS ending at i
    prev = [None] * len(nums)
    # indices[i] points to the index in nums of the tail of the subsequence of length i+1
    indices = []
    
    for i, num in enumerate(nums):
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
            indices.append(i)
        else:
            tails[pos] = num
            indices[pos] = i
        # Record the previous element in the LIS
        prev[i] = indices[pos - 1] if pos > 0 else None

    # Reconstruct the LIS backwards
    result = []
    curr = indices[-1]
    while curr is not None:
        result.append(nums[curr])
        curr = prev[curr]
    return result[::-1]

A = [5,2,3,6,3,4,7]
subsequence = []
print(lisWithSubsequence(1, A, subsequence))
print(longest_increasing_subsequence(A))