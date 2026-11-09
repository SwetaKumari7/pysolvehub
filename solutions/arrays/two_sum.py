"""Two Sum: return the indices of two values that add up to target.

Source: https://leetcode.com/problems/two-sum/
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    """Return one pair of distinct indices whose values sum to target.

    Assumes exactly one valid answer exists.
    Time: O(n) average; Space: O(n).
    """
    seen: dict[int, int] = {}
    for index, value in enumerate(nums):
        needed = target - value
        if needed in seen:
            return [seen[needed], index]
        seen[value] = index
    raise ValueError("No valid pair found")
