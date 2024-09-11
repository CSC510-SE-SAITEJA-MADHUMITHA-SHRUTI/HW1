import pytest
from hw2_debugging import merge_sort

def test_merge_sort_empty():
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    assert merge_sort([1]) == [1]

def test_merge_sort_multiple_elements():
    assert merge_sort([9, 1, 4, 1, 7, 9, 2, 6, 7, 9, 7]) == [1, 1, 2, 4, 6, 7, 7, 7, 9, 9, 9]
