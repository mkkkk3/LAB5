# Exemplary calculator tests

import pytest
import utils


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)])
def test_add(a, b, expected):
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    result = utils.divide(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "input_val, expected",
    [
        (0, "0"),
        (1, "1"),
        (2, "10"),
        (5, "101"),
        (100, "1100100"),
    ],
)
def test_to_binary_valid(input_val, expected):
    result = utils.to_binary(input_val)
    assert result == expected


@pytest.mark.parametrize("input_val", [-1, 101, 999])
def test_to_binary_out_of_range(input_val):
    with pytest.raises(ValueError, match="Input must be between 0 and 100."):
        utils.to_binary(input_val)


@pytest.mark.parametrize("input_val", [1.5, "10", None, [10], {5: "five"}])
def test_to_binary_invalid_type(input_val):
    with pytest.raises(ValueError, match="Input must be an integer."):
        utils.to_binary(input_val)
