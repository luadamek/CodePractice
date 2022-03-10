# given two sorted arrays, find their combined median
import numpy as np

# a few examples
arr1_1 = np.array([1,2,3,4,5,6,7,8]) #median 4.5
arr1_2 = np.array([1]) #median 1
median_1 = 4 #median 4

arr2_1 = np.array([1,2,3,6,7,8])
arr2_2 = np.array([4,5])
median_2 = 4.5

arr3_1 = np.array([1,2,3,10,11,12,13,14,100,101])
arr3_2 = np.array([4,5,6,7,8,9,15,16,17,18,19,20])
median_3 = np.median(np.concatenate([arr3_1, arr3_2]))

arr4_1 = np.array([1,2,3,10,11,12,13,14,100,101])
arr4_2 = np.array([4,5,6,7,8,9,15,16,17,18,19,20,21,22,23,24,25,101,102,300,400,500,600])
median_4 = np.median(np.concatenate([arr4_1, arr4_2]))

import math
#[1,2,3] len = 3, low_index = 1, high_index = 1 ( (len-1)/2) )
#[1,2,3,4] len = 4, low_index = 1, high_index = 2, ( floor((len-1)/2), ciel((len-1)/2) )
def get_median_indices(arr):
    #get the two indices needed to calculate the median of the array
    middle = (len(arr) - 1)/2
    return math.floor(middle), math.ceil(middle)

def get_median_values(arr):
    lower_index, higher_index = get_median_indices(arr)
    return arr[lower_index], arr[higher_index]

def get_median(arr):
     lower, higher = get_median_values(arr)
     return (lower + higher) / 2

#if median 1 < median 2 -->
#    cut away the lower half of arr1 including the median value, and then the same amount from the upper half of arr2
# OR cut away the upper half of arr2 including the median value, and then the same amount from the lower half of arr1
#    Do whichever cuts away the least elements

#if median 1 > median 2 -->
#    cut away the upper half of arr1 including the median value, and then the same amount from the lower half of arr2
# OR cut away the lower half of arr2 including the median value, and then the same amount from the upper half of arr1
#    Do whichever cuts away the least elements

# once again, find the median using the smaller arrays, until the arrays are reduced to a base case
# what is the base case?
# [1, 2] and [3, 4] what about this case. median 1 < median 2, then cut away lower of 1 and upper of 2 and get [2, 3] and return (2 + 3) /2 
# [1, 3] and [2, 4] then median 1 < median 2, then cut away lower half ot 1 and upper of 2 and get [3] [2]. we'd return 2 + 3 /2, whch is ok.
# what about [1, 5], [4, 4] then median 2 is contained in median 1, so return median 2
# [1,3,6] and [2,5] gives [1,2,3,5,6], then median 1 is contained in median 2, return 3 which is right
# [3] and [2, 3], then median 1 > median 3, so we get [] and [3] so 3 is the median

#base case --
# arr1 is empty, return median arr2
# arr2 is empty, return median arr1
# median values of arr1 is within median values of arr2 -> return median arr 1
# median value sof arr2 is within median values of arr2 -> return median arr 2
# len(arr1) is 1 and len(arr2) is 1: return (arr1[0] + arr2[0])/2


# what is the time complexity of this algoritm?
# getting the median of a sorted array is O(1)
# How many opertions are there? each time the shortest array is reduced by ~ half in size. This means that the 
# time complexity is O(log(min(N, M))), where N and M are the size of each array

#what is the space complexity? It is O(1), becase no copies of the arrays are made. Numpy arrays are not copied in memory when indexed.

def get_combined_median(arr1, arr2):
    assert len(arr1) > 0 or len(arr2) > 0
    if len(arr1) == 0: return get_median(arr2)
    if len(arr2) == 0: return get_median(arr1)

    lowval1, hival1 = get_median_values(arr1)
    lowval2, hival2 = get_median_values(arr2)

    if lowval1 > lowval2 and hival1 < hival2:
        return get_median(arr1)

    if lowval2 > lowval1 and hival2 < hival1:
        return get_median(arr2)

    if len(arr1) == 1 and len(arr2) == 1:
         return (arr1[0] + arr2[0]) / 2

    median1, median2 = get_median(arr1), get_median(arr2)
    low_index1, hi_index1 = get_median_indices(arr1)
    low_index2, hi_index2 = get_median_indices(arr2)

    if median1 < median2:
        n_cut = min(low_index1 + 1, len(arr2) - hi_index2)
        return get_combined_median(arr1[n_cut:], arr2[:len(arr2) - n_cut])
    elif median2 < median1:
        n_cut = min(low_index2 + 1, len(arr1) - hi_index1)
        return get_combined_median(arr2[n_cut:], arr1[:len(arr1) - n_cut])
    else:
        return median1

if __name__ == "__main__":
    assert get_median(np.array([1,2,3,4,5,6,7,8])) == 4.5
    assert get_median(np.array([1,2,3,6,7,8])) == (3 + 6) / 2
    assert get_median(np.array([1,2,3,4,5])) == 3

    assert get_combined_median(arr1_1, arr1_2) == median_1
    assert get_combined_median(arr2_1, arr2_2) == median_2
    assert get_combined_median(arr3_1, arr3_2) == median_3
    assert get_combined_median(arr4_1, arr4_2) == median_4

