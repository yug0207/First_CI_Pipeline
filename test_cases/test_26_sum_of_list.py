import importlib

module = importlib.import_module("26_sum_of_list")
sum_of_list = module.sum_of_list

def test_standard_positive_integers():
    assert sum_of_list([1, 2, 3, 4]) == 10

def test_empty_list_returns_zero():
    assert sum_of_list([]) == 0

def test_single_element():
    assert sum_of_list([7]) == 7

def test_list_with_negatives():
    assert sum_of_list([10, -5, 3, -8]) == 0

def test_list_with_floats():
    assert sum_of_list([1.5, 2.5, 3.0]) == 7.0
