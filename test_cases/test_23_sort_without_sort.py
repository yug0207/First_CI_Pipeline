import importlib

module = importlib.import_module("23_sort_without_sort")
bubble_sort = module.bubble_sort

def test_unsorted_list():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]

def test_already_sorted_list():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_empty_and_single_element_list():
    assert bubble_sort([]) == []
    assert bubble_sort([42]) == [42]

def test_list_with_duplicates_and_negatives():
    assert bubble_sort([3, -1, 2, -1, 0]) == [-1, -1, 0, 2, 3]

def test_original_list_not_modified():
    original = [5, 2, 9, 1]
    result = bubble_sort(original)
    assert original == [5, 2, 9, 1]
    assert result is not original
