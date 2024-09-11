"""
This module contains a function to generate a random array using Python's `random` module
"""

import random


def random_array(arr):
    """
    Fills an array with random numbers using Python's `random.sample`.
    
    """
    # Generate random integers between 1 and 20 and populate the input array
    random_numbers = random.sample(range(1, 21), len(arr))
    for i, _ in enumerate(arr):
        arr[i] = random_numbers[i]
    return arr


# Ensure the file ends with a newline
