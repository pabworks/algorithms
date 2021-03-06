"""Implementation of the Merge Sort algorithm.
Code is over-commented to ensure understanding.
"""
# pylint: disable=no-self-use,invalid-name
import random
import unittest

def merge_sort(array):
    """Performs recursive merge sort on an array of
    magnitude-comparable elements
    """
    # base case
    if len(array) <= 1:
        return array
    # recurse on first half of array
    a = merge_sort(array[:len(array) // 2])
    # recurse on second half of array
    b = merge_sort(array[len(array) // 2:])
    # initialise new array for the merge
    c = []
    i = 0
    j = 0
    # iterate through the elements of a and b to merge
    for _ in range(len(a) + len(b)):
        if i >= len(a):  # reach end of a
            c.append(b[j])  # iterate through b
            j += 1
        elif j >= len(b):  # reach end of b
            c.append(a[i])  # iterate through a
            i += 1
        # add smallest of two numbers as next element of c
        elif a[i] < b[j]:
            c.append(a[i])
            i += 1
        elif b[j] <= a[i]:
            c.append(b[j])
            j += 1
    return c


class TestMergeSort(unittest.TestCase):
    """Test cases for Merge Sort
    """

    def test_unique(self):
        """Tests merge sort on array with unique elements
        """
        array = list(range(0, 90))
        random.shuffle(array)
        sorted_array = merge_sort(array)
        assert sorted_array == sorted(array)

    def test_duplicates(self):
        """Tests handling of duplicates
        """
        array = [6, 4, 9, 2, 1, 2, 6, 2]
        sorted_array = merge_sort(array)
        assert sorted_array == sorted(array)

    def test_empty(self):
        """Tests empty-list edge case
        """
        assert merge_sort([]) == []

    def test_single_element(self):
        """Tests single element edge case
        """
        assert merge_sort([2]) == [2]

    def test_odd_elements(self):
        """Tests odd number of elements
        """
        array = list(range(0, 91))
        random.shuffle(array)
        sorted_array = merge_sort(array)
        assert sorted_array == sorted(array)
