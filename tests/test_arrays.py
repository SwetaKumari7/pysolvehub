from solutions.arrays.two_sum import two_sum

def test_two_sum_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_duplicate_values():
    assert two_sum([3, 3], 6) == [0, 1]

def test_two_sum_pair_later_in_list():
    assert two_sum([1, 4, 6, 8], 14) == [2, 3]
