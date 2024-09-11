"""
This module implements the merge sort algorithm to sort an array.
"""

import random


def merge_sort(arr):
    """
    This sorts the array using merge sort algorithm
    
    """
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    This merges the two sorted array into single sorted array
    
    """
    left_index = 0
    right_index = 0
    merged_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merged_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merged_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    while right_index < len(right_arr):
        merged_arr[left_index + right_index] = right_arr[right_index]
        right_index += 1

    while left_index < len(left_arr):
        merged_arr[left_index + right_index] = left_arr[left_index]
        left_index += 1

    return merged_arr


array = random.sample(range(100), 10)
arr_out = merge_sort(array)

print(arr_out)
