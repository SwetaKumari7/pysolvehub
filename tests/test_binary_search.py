from solutions.arrays.binary_search import binary_search


def test_target_in_middle():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_target_at_beginning():
    assert binary_search([1, 3, 5, 7, 9], 1) == 0


def test_target_at_end():
    assert binary_search([1, 3, 5, 7, 9], 9) == 4


def test_target_not_present():
    assert binary_search([1, 3, 5, 7, 9], 6) == -1


def test_empty_list():
    assert binary_search([], 5) == -1


def test_single_element_found():
    assert binary_search([10], 10) == 0


def test_single_element_not_found():
    assert binary_search([10], 5) == -1