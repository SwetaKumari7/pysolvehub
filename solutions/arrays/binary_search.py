# Iterative binary search for ascending sorted list.
# Source: PySolveHub issue #1: https://github.com/SwetaKumari7/pysolvehub/issues/1

# In Binary Search, we repeatedly test the middle element.

# If the middle number is less than the target, we search the right half.

# If it is larger, we search the left half.

# This repeats until the target is found or no elements remain to be searched.


def binary_search(sorted_list: list[int], target: int) -> int:
    """Return the index of target, or -1 if it is not present.

    The list that is passed in should be sorted in ascending order.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """

    left = 0
    right = len(sorted_list) - 1

    while left <= right:

        # Get the middle index of the current search range.
        middle = left + (right - left) // 2

        middle_value = sorted_list[middle]

        # Target found.
        if middle_value == target:
            return middle

        # If the target is bigger, look in the right half.
        elif middle_value < target:
            left = middle + 1

        # If the target is smaller, look in the left half.
        else:
            right = middle - 1

    # Target was not found.
    return -1