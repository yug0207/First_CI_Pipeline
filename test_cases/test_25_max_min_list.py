import importlib
import pytest

module = importlib.import_module("25_max_min_list")
find_max_min = module.find_max_min

def test_standard_list():
    assert find_max_min([4, 9, 1, 7]) == (9, 1)

def test_single_element_list():
    assert find_max_min([42]) == (42, 42)

def test_all_negative_numbers():
    assert find_max_min([-10, -5, -20, -1]) == (-1, -20)

def test_list_with_duplicates():
    assert find_max_min([5, 5, 5, 5]) == (5, 5)

def test_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        find_max_min([])
