import importlib
import pytest

module = importlib.import_module("30_decimal_to_binary")
decimal_to_binary = module.decimal_to_binary

def test_positive_integers():
    assert decimal_to_binary(10) == "1010"
    assert decimal_to_binary(1) == "1"
    assert decimal_to_binary(2) == "10"
    assert decimal_to_binary(15) == "1111"

def test_zero_returns_zero_string():
    assert decimal_to_binary(0) == "0"

def test_larger_power_of_two():
    assert decimal_to_binary(64) == "1000000"

def test_negative_number_raises_value_error():
    with pytest.raises(ValueError):
        decimal_to_binary(-1)
    with pytest.raises(ValueError):
        decimal_to_binary(-10)
