"""
Tests for mailroom
"""
import pytest

parameter_list_for_is_valid_donation = [
    ('Hi', False), (100, True), (65.43, True), (-12, False)
]


@pytest.mark.parametrize('amount, result', parameter_list_for_is_valid_donation)
def test_is_valid_donation(amount, result):
    from mailroom import is_valid_donation
    assert is_valid_donation(amount) == result
