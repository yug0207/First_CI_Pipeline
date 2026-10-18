import importlib

module = importlib.import_module("24_merge_sorted_lists")
merge_sorted_lists = module.merge_sorted_lists

def test_merge_standard_sorted_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]

def test_merge_with_empty_list():
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]
    assert merge_sorted_lists([], []) == []

def test_merge_lists_with_duplicates():
    assert merge_sorted_lists([1, 2, 2], [2, 3, 4]) == [1, 2, 2, 2, 3, 4]

def test_merge_lists_with_negative_numbers():
    assert merge_sorted_lists([-5, -1, 3], [-3, 0, 2]) == [-5, -3, -1, 0, 2, 3]

def test_merge_single_elements():
    assert merge_sorted_lists([10], [5]) == [5, 10]
