"""
This module contains a function to generate a random array using the `shuf` command
to get random numbers and populate an input array.
"""

import subprocess


def random_array(arr):
    """
    Fills an array with random numbers generated using the `shuf` command.
    
    """
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr


# Ensure the file ends with a newline
