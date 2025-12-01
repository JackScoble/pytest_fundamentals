from pytest import approx
import pytest
import os
import sys
from triangle import area_of_a_triangle


def test_float_values_exact():
    """ Test areas when inputs are floats"""
    assert area_of_a_triangle(2.3, 5.7) == 6.555
    
def test_float_values_approx():
    """Test areas when inputs and output are floats using approx"""
    # these tests will fail without approx
    assert 0.1 + 0.2 == approx(0.3) 
    assert area_of_a_triangle(3.4556, 8.3567) == approx(14.43870626)
    assert area_of_a_triangle(3.4556, 8.3567) == approx(14.43, rel=1e-3)

def test_integer_values():
    """ Test areas when values are integers """
    assert area_of_a_triangle(2, 5) == 5

def test_zero_base():
    """ Test areas when base is zero """
    assert area_of_a_triangle(0, 5) == 0

def test_zero_height():
    """ Test areas when height is zero """
    assert area_of_a_triangle(5, 0) == 0

def test_zero_values():
    """ Test areas when base and height are zero """
    assert area_of_a_triangle(0, 0) == 0

def test_negative_base():
    """ Test that ValueError is raised when base is negative """
    with pytest.raises(ValueError):
        area_of_a_triangle(-2, 5)

def test_negative_height():
    """ Test that ValueError is raised when height is negative """
    with pytest.raises(ValueError):
        area_of_a_triangle(2, -5)

def test_negative_values():
    """ Test that ValueError is raised when both are negative """
    with pytest.raises(ValueError):
        area_of_a_triangle(-2, -5)

def test_with_boolean():
    """ Test that TypeError is raised with boolean types """
    with pytest.raises(TypeError):
        area_of_a_triangle(True, 5)
    with pytest.raises(TypeError):
        area_of_a_triangle(5, False)

def test_with_string():
    """ Test that TypeError is raised with string types """
    with pytest.raises(TypeError):
        area_of_a_triangle('base', 5)
    with pytest.raises(TypeError):
        area_of_a_triangle(5, 'height')

def test_with_nulls():
    """ Test that TypeError is raised with null types """
    with pytest.raises(TypeError):
        area_of_a_triangle(None, 5)
    with pytest.raises(TypeError):
        area_of_a_triangle(5, None)

def test_with_lists():
    """ Test that TypeError is raised with list types """
    with pytest.raises(TypeError):
        area_of_a_triangle([2], 5)
    with pytest.raises(TypeError):
        area_of_a_triangle(5, [5])

def test_with_tuples():
    """ Test that TypeError is raised with tuple types """
    with pytest.raises(TypeError):
        area_of_a_triangle((2,), 5)
    with pytest.raises(TypeError):
        area_of_a_triangle(5, (5,))

def test_with_dicts():
    """ Test that TypeError is raised with dict types """
    with pytest.raises(TypeError):
        area_of_a_triangle({'base': 2}, 5)
    with pytest.raises(TypeError):
        area_of_a_triangle(5, {'height': 5})

def test_with_sets():
    """ Test that TypeError is raised with set types """
    with pytest.raises(TypeError):
        area_of_a_triangle({2}, 5)
    with pytest.raises(TypeError):
        area_of_a_triangle(5, {5})

def test_with_complex_numbers():
    """ Test that TypeError is raised with complex number types """
    with pytest.raises(TypeError):
        area_of_a_triangle(2 + 3j, 5)
    with pytest.raises(TypeError):
        area_of_a_triangle(5, 4 + 5j)

def test_large_values():
    """ Test areas when inputs are large numbers """
    assert area_of_a_triangle(1e6, 2e6) == 1e12

def test_small_values():
    """ Test areas when inputs are small numbers """
    assert area_of_a_triangle(1e-6, 2e-6) == 1e-12

def test_mixed_values():
    """ Test areas when one input is integer and the other is float """
    assert area_of_a_triangle(5, 2.5) == 6.25
    assert area_of_a_triangle(3.5, 4) == 7.0

def test_area_symmetry():
    """ Test that area is the same regardless of the order of base and height """
    assert area_of_a_triangle(4, 6) == area_of_a_triangle(6, 4)

def test_area_with_identical_base_height():
    """ Test area when base and height are identical """
    assert area_of_a_triangle(5, 5) == 12.5


@pytest.mark.skip(reason="Demonstration of pytest.mark.skip: test not applicable right now")
def test_skipped_mark():
    """A test that is always skipped using @pytest.mark.skip"""
    assert area_of_a_triangle(10, 2) == 10


@pytest.mark.skipif(os.getenv("SKIP_TRIANGLE") == "1", reason="Environment requested skip")
def test_skip_if_env_variable():
    """A test that is skipped if the environment variable SKIP_TRIANGLE is set to 1"""
    assert area_of_a_triangle(5, 5) == 12.5


def test_dynamic_skip_at_runtime():
    """A test that chooses to skip at runtime for demonstration (skips on non-Linux platforms)"""
    if sys.platform != "linux":
        pytest.skip("This demonstration test only runs on Linux")
    assert area_of_a_triangle(6, 2) == 6
