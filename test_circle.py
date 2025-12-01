from pytest import approx
import pytest
import os
import sys
from circle import area_of_a_circle


def test_float_values_exact():
    """ Test areas when inputs are floats"""
    # 1.0 -> area is pi
    assert area_of_a_circle(1.0) == approx(3.14159265, rel=1e-7)


def test_float_values_approx():
    """Test areas when inputs and output are floats using approx"""
    # these tests will fail without approx
    assert area_of_a_circle(0.1) == approx(3.14159265 * 0.01, rel=1e-7)
    assert area_of_a_circle(2.5) == approx(19.634954084936208)


def test_integer_values():
    """ Test areas when values are integers """
    assert area_of_a_circle(1) == approx(3.14159265, rel=1e-7)


def test_zero_radius():
    """ Test areas when radius is zero """
    assert area_of_a_circle(0) == 0


def test_negative_radius():
    """ Test that ValueError is raised when radius is negative """
    with pytest.raises(ValueError):
        area_of_a_circle(-1)


def test_with_boolean():
    """ Test that TypeError is raised with boolean types """
    with pytest.raises(TypeError):
        area_of_a_circle(True)
    with pytest.raises(TypeError):
        area_of_a_circle(False)


def test_with_string():
    """ Test that TypeError is raised with string types """
    with pytest.raises(TypeError):
        area_of_a_circle('radius')


def test_with_nulls():
    """ Test that TypeError is raised with null types """
    with pytest.raises(TypeError):
        area_of_a_circle(None)


def test_with_lists():
    """ Test that TypeError is raised with list types """
    with pytest.raises(TypeError):
        area_of_a_circle([2])


def test_with_tuples():
    """ Test that TypeError is raised with tuple types """
    with pytest.raises(TypeError):
        area_of_a_circle((2,))


def test_with_dicts():
    """ Test that TypeError is raised with dict types """
    with pytest.raises(TypeError):
        area_of_a_circle({'radius': 2})


def test_with_sets():
    """ Test that TypeError is raised with set types """
    with pytest.raises(TypeError):
        area_of_a_circle({2})


def test_with_complex_numbers():
    """ Test that TypeError is raised with complex number types """
    with pytest.raises(TypeError):
        area_of_a_circle(2 + 3j)


def test_large_values():
    """ Test areas when inputs are large numbers """
    assert area_of_a_circle(1e6) == approx(3.141592653589793 * 1e12)


def test_small_values():
    """ Test areas when inputs are small numbers """
    assert area_of_a_circle(1e-6) == approx(3.141592653589793 * 1e-12)


def test_area_consistency():
    """Test that area behaves consistently for radius variations"""
    assert area_of_a_circle(2) == approx(12.566370614359172)
    assert area_of_a_circle(3) == approx(28.274333882308138)


@pytest.mark.skip(reason="Demonstration of pytest.mark.skip: test not applicable right now")
def test_skipped_mark():
    """A test that is always skipped using @pytest.mark.skip"""
    assert area_of_a_circle(10) == approx(314.1592653589793)


@pytest.mark.skipif(os.getenv("SKIP_CIRCLE") == "1", reason="Environment requested skip")
def test_skip_if_env_variable():
    """A test that is skipped if the environment variable SKIP_CIRCLE is set to 1"""
    # radius 5 -> 25*pi
    assert area_of_a_circle(5) == approx(78.53981633974483)


def test_dynamic_skip_at_runtime():
    """A test that chooses to skip at runtime for demonstration (skips on non-Linux platforms)"""
    if sys.platform != "linux":
        pytest.skip("This demonstration test only runs on Linux")
    assert area_of_a_circle(2) == approx(12.566370614359172)
