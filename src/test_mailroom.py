"""
Tests for mailroom
"""
import pytest

test_names = ['Carlos', 'Elyanil']
test_amount = [100, 200]

parameter_list_for_create_email = [
    (test_names[0], test_amount[0], 'Thank you {} for {} dollars'.format(test_names[0], test_amount[0])),
    (test_names[1], test_amount[1], 'Thank you {} for {} dollars'.format(test_names[1], test_amount[1]))
]

parameter_list_for_is_valid_donation = [
    ('Hi', False), (100, True), (65.43, True), (-12, False)
]

@pytest.mark.parametrize("name, amount, result", parameter_list_for_create_email)
def test_create_email(name, amount):
    from mailroom import create_email
    assert create_email(name, amount) == result


@pytest.mark.parametrize('amount, result', parameter_list_for_is_valid_donation)
def test_is_valid_donation(amount, result):
    from mailroom import is_valid_donation
    assert is_valid_donation(amount) == result
