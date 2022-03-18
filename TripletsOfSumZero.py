'''
given a list of integers, find all triplets of three numbers that sum to zero. Do not include
duplicate numbers
'''

test_1 = [1,2,3,4,5]
result_1 = []

test_2 = [-1, -1, 0, 1, 2]
result_2 = [[-1,-1,2],[-1,0,1]]

test_3 = [-3,-1, -1, 0, 1, 2, 4]
result_3 = [[-3,-1,4],[-3,1,2],[-1,-1,2],[-1,0,1]]

def build_frequency_map(nums):
    frequency_map = {}
    for n in nums:
        if n not in frequency_map: frequency_map[n] = 0
        else: frequency_map[n] += 1
    return frequency_map

def check_enough_numbers(fmap1, fmap2):
    for key in fmap1:
        if key not in fmap2: return False
        if fmap2[key] < fmap1[key]: return False
    return True

#this function runs in O(N^2) time
def find_triplets(nums):
    if len(nums) < 3: return []

    triplets = []
    fmap = build_frequency_map(nums) #O(N)
    doublets = {}
    for i in range(0, len(nums)-1): #O(N)
        for j in range(i+1, len(nums)): #O(N^2) with the previous loop
            doublets[(i,j)] = nums[i] + nums[j]

    found_triplets = set()
    for pair in doublets:
        target = -1 * doublets[pair]
        index_1 = pair[0]
        index_2 = pair[1]
        num_1 = nums[index_1]
        num_2 = nums[index_2]
        if target < num_1 or target < num_2: continue

        triplet = [num_1, num_2, target]
        triplet_tuple = tuple(triplet)
        this_fmap = build_frequency_map(triplet)
        if check_enough_numbers(this_fmap, fmap) and not triplet_tuple in found_triplets:
           triplets.append(triplet)
           found_triplets.add(triplet_tuple)

    return triplets

#this function runs in O(N^3) time
def find_triplets_cubic(nums):
    if len(nums) < 3: return []

    triplets = []
    found_triplets = set()
    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                triplet = [nums[i], nums[j], nums[k]]
                triplet_tuple = tuple(triplet)
                if sum(triplet) == 0 and not triplet_tuple in found_triplets:
                    triplets.append(triplet)
                    found_triplets.add(triplet_tuple)

    return triplets


import numpy as np
assert find_triplets(test_1) == result_1
assert find_triplets(test_2) == result_2
assert find_triplets(test_3) == result_3
print(find_triplets_cubic(np.arange(-200, 200)))



