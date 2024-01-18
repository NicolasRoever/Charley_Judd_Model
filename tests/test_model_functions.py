import pytest
import numpy as np

from src.chamley_judd_model_implementation.model_functions import ces_utility_function


import pytest

def test_ces_utility():
    """ This function tests the CES utility function with some values."""
    consumption = 100
    leisure = 100
    sigma = 0.5

    expected_output = 2

    actual_output = ces_utility_function(consumption, leisure, sigma)

    assert np.isclose(actual_output, expected_output)
