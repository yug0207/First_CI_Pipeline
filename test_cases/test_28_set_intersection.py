import importlib

module = importlib.import_module("28_set_intersection")
set_intersection = module.set_intersection

def test_overlapping_sets():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}

def test_disjoint_sets():
    assert set_intersection({1, 2}, {3, 4}) == set()

def test_identical_sets():
    assert set_intersection({1, 2, 3}, {1, 2, 3}) == {1, 2, 3}

def test_with_empty_set():
    assert set_intersection(set(), {1, 2}) == set()
    assert set_intersection({1, 2}, set()) == set()

def test_string_elements():
    assert set_intersection({"apple", "banana"}, {"banana", "cherry"}) == {"banana"}
