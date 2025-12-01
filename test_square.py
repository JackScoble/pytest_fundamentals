from pytest import approx
import pytest
import os
import sys
from square import area_of_a_square


def test_float_values_exact():
    """ Test areas when inputs are floats"""
    assert area_of_a_square(2.5) == approx(6.25)


def test_float_values_approx():
    """Test areas when inputs and output are floats using approx"""
    assert area_of_a_square(1.1) == approx(1.21)


def test_integer_values():
    """ Test areas when values are integers """
    assert area_of_a_square(2) == 4


def test_zero_side():
    """ Test areas when side is zero """
    assert area_of_a_square(0) == 0


def test_negative_side():
    """ Test that ValueError is raised when side is negative """
    with pytest.raises(ValueError):
        area_of_a_square(-2)


def test_with_boolean():
    """ Test that TypeError is raised with boolean types """
    with pytest.raises(TypeError):
        area_of_a_square(True)
    with pytest.raises(TypeError):
        area_of_a_square(False)


def test_with_string():
    """ Test that TypeError is raised with string types """
    with pytest.raises(TypeError):
        area_of_a_square('side')


def test_with_nulls():
    """ Test that TypeError is raised with null types """
    with pytest.raises(TypeError):
        area_of_a_square(None)


def test_with_lists():
    """ Test that TypeError is raised with list types """
    with pytest.raises(TypeError):
        area_of_a_square([2])


def test_with_tuples():
    """ Test that TypeError is raised with tuple types """
    with pytest.raises(TypeError):
        area_of_a_square((2,))


def test_with_dicts():
    """ Test that TypeError is raised with dict types """
    with pytest.raises(TypeError):
        area_of_a_square({'side': 2})


def test_with_sets():
    """ Test that TypeError is raised with set types """
    with pytest.raises(TypeError):
        area_of_a_square({2})


def test_with_complex_numbers():
    """ Test that TypeError is raised with complex number types """
    with pytest.raises(TypeError):
        area_of_a_square(2 + 3j)


def test_large_values():
    """ Test areas when inputs are large numbers """
    assert area_of_a_square(1e6) == 1e12


def test_small_values():
    """ Test areas when inputs are small numbers """
    assert area_of_a_square(1e-6) == 1e-12


def test_area_consistency():
    """Test that area behaves consistently for side variations"""
    assert area_of_a_square(4) == 16
    assert area_of_a_square(5) == 25


@pytest.mark.skip(reason="Demonstration of pytest.mark.skip: test not applicable right now")
def test_skipped_mark():
    """A test that is always skipped using @pytest.mark.skip"""
    assert area_of_a_square(10) == 100


@pytest.mark.skipif(os.getenv("SKIP_SQUARE") == "1", reason="Environment requested skip")
def test_skip_if_env_variable():
    """Test that is skipped via env var"""
    assert area_of_a_square(3) == 9


def test_dynamic_skip_at_runtime():
    """A test that chooses to skip at runtime for demonstration (skips on non-Linux platforms)"""
    if sys.platform != "linux":
        pytest.skip("This demonstration test only runs on Linux")
    assert area_of_a_square(2) == 4
